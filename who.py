from bs4 import BeautifulSoup
import requests
import sqlite3

con = sqlite3.connect("gho.sqlite")
c = con.cursor()
c.execute("""
drop table if exists gho
""")
con.commit()
c.execute("""
create table gho(
GHO text,
PublishState text,
Year text,
Region text,
Country text,
DisplayValue float,
NumbericValue float)
""")
con.commit()

url = "http://apps.who.int/gho/athena/data/GHO/MDG_0000000016.html?profile=ztable&filter=COUNTRY:*;REGION:*"

r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
GHO = ""
PublishState = ""
Year = ""
Region = ""
Country = ""
DisplayValue = ""
NumbericValue = ""

table = soup.findAll("tr")[1:]
for rows in table:
	cells = rows.findAll("td")
	if len(rows) > 0:
		GHO = cells[0].find(text = True)
		PublishState = cells[1].find(text = True)
		Year = cells[2].find(text = True)
		Region = cells[3].find(text = True)
		Country = cells[4].find(text = True)
		DisplayValue = cells[5].find(text = True)
		NumbericValue = cells[6].find(text = True)
		
		print(GHO,PublishState,Year,Region,Country,DisplayValue,NumbericValue)
		
		c.execute("""
		insert into gho (GHO,PublishState,Year,Region,Country,DisplayValue,NumbericValue) values (?,?,?,?,?,?,?)""",(GHO,PublishState,Year,Region,Country,DisplayValue,NumbericValue,))
		con.commit()


