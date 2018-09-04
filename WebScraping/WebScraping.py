import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)

# Get the title
title = soup.title
print(title)

# Print out the text
text = soup.get_text()
#print(soup.text)

# Extract all link tags <a>

''''all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))

# Print the first 10 rows for sanity check

print(rows[:10])'''

rows = soup.find_all('tr')

cleantext_list = []

for row in rows:
    row_td = row.find_all('td')
    str_cells = str(row_td)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    cleantext_list.append(cleantext)

df = pd.DataFrame(cleantext_list)
df1 = df[0].str.split(',', expand=True)
df1[0] = df1[0].str.strip('[')
df1[df1.columns[-1]] = df1.iloc[:,-1].str.strip(']')

col_labels = soup.find_all('th')

all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
df2 = pd.DataFrame(all_header)
df3 = df2[0].str.split(',', expand=True)

df3[0] = df3[0].str.strip('[')
df3[df3.columns[-1]] = df3.iloc[:,-1].str.strip(']')


frames = [df3, df1]
df4 = pd.concat(frames)

df5 = df4.rename(columns=df4.iloc[0])
df6 = df5.dropna(axis=0, how='any')
df7 = df6.drop(df6.index[0])

print(df7.head(10))



