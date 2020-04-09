# init: 200401 by KWC

import pandas as pd 



# Read in the data
fName = 'agreement_signed.xlsx'
df = pd.read_excel(fName) # Requires xlrd

# Basic stats
print('Number of members:', len(df))
print('Number of Institutions:', len(set(df['Institution'])))
print('Number of Countries:', len(set(df['Country'])))

'''
#200406
Number of members: 320
Number of Institutions: 273
Number of Countries: 40
'''

# Generate a text file of the members for the website:
print('Generating members list website file...')
with open("mems.txt", "w") as f: 
	html = '<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n'
	for index, row in df.iterrows():
		f.write(html.format(row['Full name'], row['Institution'], row['Country'])) 



# Generate file for the members map: