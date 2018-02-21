import urllib.request
from bs4 import BeautifulSoup
import requests

urlKontrol = 'https://www.hepsiburada.com'  #url kontrolu için tutulan değişken
url = input("url: ")

r = requests.get(url)                       #http response code
httpHeaders = r.status_code                 #http response code

if url[0:27] == urlKontrol[0:27] and httpHeaders == 200:
    print('url Başarılı')
else:
    print('url Başarısız')

request = urllib.request.Request(url)       #url'ye istek
response = urllib.request.urlopen(request)  #isteğin cevaplanması
the_page = response.read()                  #sayfa okuma
theText = the_page.decode('utf-8')          #alınan sayfanın utf-8 dönüştürümü

soup = BeautifulSoup(theText, 'html.parser')

for i in soup.find_all('span', {"data-bind": "markupText:'currentPriceBeforePoint'"}):
    for j in soup.find_all('span', {"data-bind": "markupText:'currentPriceAfterPoint'"}):
        print("Sonuç:",i.text+','+j.text,"TL")




