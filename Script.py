import urllib.request
from bs4 import BeautifulSoup
import requests
import sys

url = input("url: ")

try:
    r = requests.get(url)                        #http response code
    httpHeaders = r.status_code                  #http response code
except Exception as e:
    print('Başarısız url')
    sys.exit(0)

if httpHeaders == 200:

    request = urllib.request.Request(url)       # url'ye istek
    response = urllib.request.urlopen(request)  # isteğin cevaplanması
    the_page = response.read()                  # sayfa okuma
    theText = the_page.decode('utf-8')          # alınan sayfanın utf-8 dönüştürümü

    soup = BeautifulSoup(theText, 'html.parser')

    for i in soup.find_all('span', {"data-bind": "markupText:'currentPriceBeforePoint'"}):
        for j in soup.find_all('span', {"data-bind": "markupText:'currentPriceAfterPoint'"}):
            print("Sonuç:", i.text + ',' + j.text, "TL")

else:
    print('Başarısız url')




