import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text,'html.parser')
#print(soup)

# parliment constituency general table only Headings
table = soup.find("table",class_= "table")
#print(table)

headers = table.find_all("th")
#print(headers)

titles = []
for i in headers:
    title = i.text
    titles.append(title)
#print(titles)

df = pd.DataFrame(columns=titles)
#print(df)

rows = table.find_all("tr")
#print(rows)

# for i in rows[1:]:
#     print(i.text)
    
for i in rows[1:]:
    data = i.find_all("td")
    #print(data)
    row = [tr.text for tr in data]
    #print(row)  
    l = len(df)
    df.loc[l] = row 
    
# new = ['IND',7]    

# df = df.append(pd.Series(new,index=df.columns[:len(new)]) , ignore_index= True)
print(df)

df.to_csv("Election commision of india.csv")
    