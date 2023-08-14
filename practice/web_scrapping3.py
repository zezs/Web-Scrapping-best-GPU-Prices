from bs4 import BeautifulSoup
import requests                                 # navigatethe tree,
                                                # access parent, sibling, content etc..
url = "https://coinmarketcap.com/"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tablebody = doc.tbody
trs = tablebody.contents

prices = {}

for tr in trs[:10]:                         # parsing through tablerows(trs) using element tr
    name, price = tr.contents[2:4]          # assigning tr  conents into name and price
      
    fixed_name = name.p.string
    fixed_price = price.a.string

    prices[fixed_name] = fixed_price

    print(prices)
    
    #print(name.p.string)
    #print(price.a.string)



"""print(trs[1].next_sibling)
print(trs[1].previous_sibling)
                                       #CHECK THE NET
print(list(trs[0].contents))"""        #.descenants -> tags + content
                                       #.contents  -> gives content
                                       #.child -> only tags

"""prices = {}          # printing only name and price of all coins

for tr in trs:
    for td in tr.contents[2: 4]:
        print(td)"""