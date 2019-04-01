import requests
from bs4 import BeautifulSoup

session = requests.session()
headers = {"User-Agent": "Chrome", "Accept":"text/html, application/xhtml+xml, application/xml; q=0.9, image/webp, */*; q=0.8"}
url = "https://finance.yahoo.com/quote/601318.SS?p=601318.SS&.tsrc=fin-srch"
req = session.get (url, headers=headers)

bsObj = BeautifulSoup(req.text, 'html.parser')
print (bsObj.prettify())

