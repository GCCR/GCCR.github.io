import os
import re
import logging
import pandas as pd
from googleapiclient.discovery import build
import yaml
from common import WEBSITES

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

def member_url(member):
    name, *rest = member.split(" (")
    name = "".join(name)
    try:
        url = WEBSITES[name]
    except KeyError:
        return member
    rest = f' ({"".join(rest)}' if rest else ""
    return f'<a href="{url}">{name}</a>{rest}'

# fetch Google Sheet for members data
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
COMMITTEES_SPREADSHEET_ID = os.environ["COMMITTEES_SPREADSHEET_ID"]
service = build("sheets", "v4", developerKey=GOOGLE_API_KEY)
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=COMMITTEES_SPREADSHEET_ID,
                            range='Sheet1').execute()
values = result.get('values', [])

# to dataframe
columns = []
for col in values[0]:
    *name, time = col.split()
    columns.append((" ".join(name), time.capitalize()))
n_cols = len(columns)
columns = pd.MultiIndex.from_tuples(columns, names=["Committee", "Time"])
data = []
for row in values[1:]:
    n = len(row)
    row = [x if x else None for x in row]
    padded = row + [None for _ in range(n_cols - n)]
    data.append(padded)
df = pd.DataFrame(data, columns=columns)

# write yaml
content = {}
for committee in df.columns[1:].droplevel(1).drop_duplicates():
    content[committee] = {}
    for time in df[committee].columns:
        col = (committee, time)
        members = df[col].dropna().to_list()
        if members:
            content[committee][time] = [member_url(m) for m in members]
    if not content[committee]:
        content.pop(committee)

with open("_data/committees.yml", "w") as f:
    for committee, items in content.items():
        f.write(f"- committee: {committee}\n")
        f.write(f"  listing:\n")
        for time, members in items.items():
            f.write(f"  - time: {time}\n")
            f.write(f"    members: {members}\n")