#içeri aktarilan kutuphaneler
from bs4 import BeautifulSoup
import requests
import csv
import time
import urllib
import os
import urllib.request

# Baglanacagimiz site
url = "https://www.ucdortbes.com/videolar/ayt-matematik-soru-bankasi"
# Siteye baglanti kurmak icin istekte bulunuyoruz
sayfa = urllib.request.urlopen(url)
soup = BeautifulSoup(sayfa,"html.parser")
#print(soup.prettify)
print("'' >>> HTML KODU CEKILDI")

#listeler
liste=[]
urls=[]
links=[]
#parse islemleri
body=soup.find("div",{"class":"container container_single"})
row_player=body.find("div",{"class":"row row_player"})
pr_zero=row_player.find("div",{"class":"col-md-4 column pr_zero"})
scroll=pr_zero.find("div",{"id":"lazy_galeri"})
for i in scroll.findAll("li"):
    liste.append(i)
for i in range(len(liste)):
    for k in liste[i].findAll("li"):
        urls.append(k)
urls.pop(0)
for i in range(len(urls)):
    links.append(urls[i].a["href"])
link_dosya=open("linkler.txt","w")
for i in range(len(links)):
    link_dosya.write(links[i]+"\n")
link_dosya.close()    
print(links[0])
