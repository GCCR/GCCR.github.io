# imports
import os, re, logging
from datetime import datetime
import html
import pandas as pd
import geopandas as gpd
import seaborn as sns
import bokeh
from bokeh.io import output_file, save, export_png
from bokeh.plotting import figure
from bokeh.models import (
    GeoJSONDataSource, ColumnDataSource, HoverTool, ColorBar, WheelZoomTool,
    LinearColorMapper, CategoricalColorMapper, Legend, LegendItem, Title,
)
from googleapiclient.discovery import build
import geckodriver_autoinstaller
from common import WEBSITES


logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# install geckodriver
geckodriver_autoinstaller.install()

# read country shapes
def country_reader(path):
    geo = gpd.read_file(os.path.join("_scripts/natural-earth-vector", path))
    # restrict to the columns needed
    geo = geo[['NAME_CIAWF', 'GEOUNIT', 'geometry', 'CONTINENT']]
    geo.columns = ['Country', 'Long name', 'geometry', 'Continent']
    geo["Country"].fillna(geo["Long name"], inplace=True)
    geo.drop(columns="Long name", inplace=True)
    return geo

details = country_reader("ne_50m_admin_0_sovereignty.shp")
geo = country_reader("ne_110m_admin_0_sovereignty.shp")
missing = details.loc[~details["Country"].isin(geo["Country"])]
geo = geo.append(missing)
geo.reset_index(inplace=True, drop=True)

# drop Antarctica
geo = geo.loc[~(geo['Country'] == 'Antarctica')]
# correct names
geo.loc[geo["Country"]=="Cote D'ivoire","Country"] = "Cote d'Ivoire"
geo.loc[geo["Country"]=="Baykonur Cosmodrome","Country"] = "Kazakhstan"

print(len(geo), "countries available for the map")

# fetch Google Sheet for members data
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
SPREADSHEET_ID = os.environ["SPREADSHEET_ID"]
service = build("sheets", "v4", developerKey=GOOGLE_API_KEY)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                            range='A:D').execute()
values = result.get('values', [])
members = pd.DataFrame(values[1:], columns=values[0])
# remove empty lines
empty = members[members["Full name"].isnull()]
if len(empty) != 0:
	print(f"Found {len(empty)} row(s) without a member's name")
	members.dropna(subset=["Full name"], inplace=True)
	print("Lines with empty member's name dropped")
# set columns
members = members[["Full name","Institution","Country of Institution"]]
members.columns = ["Member","Institution","Country"]

# correct country names to be the same as natural-earth-vector
countries_dict = {
	# name in form: name in natural-earth-vector
    "Gambia": "Gambia, The",
    "Swaziland": "eSwatini",
    "United States": "United States of America",
    "Czech Republic": "Czechia",
}
members["Country"] = members["Country"].apply(lambda x: countries_dict.get(x, x))

# capitalize names
def capitalize(x):
    return "".join(i.title() for i in re.split(r'(Ma?c)[A-Z]', x))
members["Member"] = members["Member"].apply(capitalize)

# check for duplicates
duplicates = members.loc[members.duplicated(subset="Member", keep=False)]
if len(duplicates) != 0:
	print("Duplicated members were found:")
	print(duplicates)
	members.drop_duplicates(subset="Member", keep="last", inplace=True)
	print("Duplicated members corrected")

# print total
print("***")
print(len(members), "members registered in", members["Country"].nunique(), "countries and", members["Institution"].nunique(), "institutions")
print("***")

# group members by country
group = members.groupby("Country", as_index=False).agg({"Member":"count"}).rename(columns={"Member": "N_members"})

# merge country shapes and members
df = geo.merge(group, on="Country", how="left")
df["N_members"] = df["N_members"].fillna(0).astype(int)

# check if we lost some members when merging
assert group["N_members"].sum() == df["N_members"].sum(), f"""\
Something is wrong with the number of members: {group['N_members'].sum()} != {df['N_members'].sum()}
This is likely due to a mismatch between the country names used by the form and natural-earth-vector.
Please check the countries added since the last update, and the list below. If a mismatch is found,
update the `countries_dict` variable. If you're not sure, contact your Python guru Cédric Bouysset
Country names used by natural-earth-vector:
{geo["Country"]}
"""

# standardize country names for the map
def standardize(x):
    x = str(x).strip()
    return html.escape(x)
df["Country"] = df["Country"].apply(standardize)

# create the map
output_file("assets/html/members-map.html", title="GCCR members", mode="inline")
p = figure(
    height=550, width=950,
    title="Members of the Global Consortium for Chemosensory Research",
    toolbar_location=None, tools="pan", toolbar_sticky=False,
)
p.title.text_font_size = '15pt'
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.axis.visible = False
# Add hover tool
hover = HoverTool(
    tooltips=[
        ('Country', '@Country{safe}'),
        ('Number of members','@N_members'),
    ])
p.add_tools(hover)
# Add wheel zoom
zoom = WheelZoomTool(zoom_on_axis=False)
p.add_tools(zoom)
# activate them
p.toolbar.active_inspect = hover
p.toolbar.active_scroll = zoom
# colormap
bins = ["No members", "1-5", ">5"]
palette = ["#f2f2f2"] + sns.color_palette("Greens", len(bins)-1).as_hex()
cmap = CategoricalColorMapper(palette=palette, factors=bins)
source = df.copy()
source["bin"] = pd.cut(source["N_members"], bins=[-1, 1 -1, 5 +1, source["N_members"].max()], labels=bins)
# Add patches (countries) to the figure
renderers = []
for label in bins:
    r = p.patches(
        'xs','ys', source=GeoJSONDataSource(geojson=source[source["bin"] == label].to_json()),
        fill_color={'field': "bin", 'transform': cmap},
        line_color='black', line_width=0.25, fill_alpha=1,
        hover_line_width=2,
    )
    renderers.append(r)
# legend
legend = Legend(border_line_width=0, spacing=20, items=[
    LegendItem(label=label, renderers=[renderers[i]], index=i) for i,label in enumerate(bins)
], location="center_left", orientation="horizontal", title="Number of members")
p.add_layout(legend, "below")
# date of update
last_update = Title(
    text=f"Last update: {datetime.now().strftime('%B %d, %Y')} - {len(members)} members in {members['Country'].nunique()} countries",
    text_font_size='10pt'
)
p.add_layout(last_update, "below")
# export to png (might fail)
try:
	export_png(p, filename="assets/img/members-map.png", width=950, height=600)
except Exception as e:
	print("Skipped the creation of a PNG of the map as an error occured:")
	print(e)
# export HTML
p.sizing_mode = "scale_width"
save(p)

# create summary table of members
df = geo.merge(members, on="Country", how="left")
df.drop(columns=["geometry","Institution"], inplace=True)
df = df.groupby(["Continent", "Country"]).agg({"Member":"count"}).rename(columns={"Member": "Number of members"}).sort_values(["Continent", "Number of members", "Country"], ascending=[True, False, True])
df = df[df["Number of members"] > 0]
df.to_excel("assets/data/members-summary.xlsx")

# add website url to some members
for name, url in WEBSITES.items():
	members.loc[members["Member"] == name, "Website"] = url

# standardize strings for HTML and YAML
def standardize(x):
    x = str(x).strip()
    x = x.replace(":", "")
    x = html.escape(x)
    if x.startswith("&"):
        x = '"%s"' % x
    return x

for col in ["Country", "Member", "Institution"]:
    members[col] = members[col].apply(standardize)

# output YML file
def pandas_row_to_yml(s):
	x = f"- name: {s['Member']}\n  institution: {s['Institution']}\n  country: {s['Country']}\n"
	if pd.notna(s["Website"]):
		x += f"  url: {s['Website']}\n"
	return x
with open("_data/members.yml", "w") as f:
	for i, row in members.iterrows():
		f.write(pandas_row_to_yml(row))
print("Done")
