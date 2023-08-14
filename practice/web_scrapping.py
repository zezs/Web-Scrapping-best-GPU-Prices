from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-ti-gv-n308teagle-12gd/p/1FT-000A-002K7"

result = requests.get(url)
doc = BeautifulSoup(result.text,"html.parser")
#print(doc.prettify())

prices = doc.find_all(text="$")
parent = prices[0].parent
strong_tag = parent.find("strong")
#print(strong_tag.string)
print(prices)
print(parent)
print(strong_tag.string)



"""with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags =  doc.find_all("p")[0]
print(tags)"""



























"""print(doc.prettify())
tag = doc.find("p")
tags = doc.find("i")
b_tags = tags.find_all("b")
print(tags.string)
print("****************")
print(tag.prettify)
print("****************")
print(tags)
print("-------After alterining-----")
tag.string = "hello"
print(tag.string)
print("++++++++++++++=Document+++++++++++")
print(doc)"""