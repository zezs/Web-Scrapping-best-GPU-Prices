from bs4 import BeautifulSoup
import re

with open("index2.html",'r') as f:                    #find_all : value = tagname; 
    doc = BeautifulSoup(f, "html.parser")            #attr of input tags: type(text, password, email..), name, placeholder
                                                    #TEXT = value in tags which can be displayed

tags = doc.find_all("input", type = "text")
for tag in tags:
    tag['placeholder'] = "I changed you!"

with open("changed.html", "w") as file:
    file.write(str(doc))

print(tags)


"""tag = doc.find_all(["option"], value = "undergraduate", text = "Undergraduate")
tags = doc.find_all(class_="btn-item")
print(tag[0].string)
print(tags)"""

"""tags = doc.find_all(text=re.compile("\$.*"), limit = 1) # \ --> after dollar: $-> find $; .* -> any no. of char after $; 
for tag in tags:
    print(tag.strip())
#print(tags)"""

