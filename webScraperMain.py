from bs4 import BeautifulSoup as bsoup
import requests

class Article:
    def __init__(self,cat,titl,aut,summ):
        self.list=[cat,titl,aut,summ]



source= requests.get("https://www.quantamagazine.org/archive/").content
soup=bsoup(source,"lxml")


with open("articles.csv","w") as f:
    headers="Category,Title,Author,Summary\n"
    f.write(headers)
    cats=soup.findAll("a",{"class":"kicker"})
    titls=soup.findAll("h2",{"class":"card__title"})
    auts=soup.findAll("span",{"class":"byline__author"})
    summs=soup.findAll("div",{"class":"card__excerpt"})
    for n in range(len(titls)):
        tempArt=Article(cats[n],titls[n],auts[n],summs[n])
        for entry in tempArt.list:
            f.write(str(entry.text).replace(",","|")+",")
        f.write("\n")
    f.close()
