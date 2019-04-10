#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


class instrument:

  def __init__(self, id):
    self.id = id

  def displaySimple(self):
      print ('{:^6} {:8.2f} {:6.2f}%'.format(self.id, self.previousClose, self.change))

  def query(self):
    session = requests.session()
    headers = {"User-Agent": "Chrome", "Accept":"text/html, application/xhtml+xml, application/xml; q=0.9, image/webp, */*; q=0.8"}
    url = "http://hq.sinajs.cn/list=" + self.id
    req = session.get (url, headers=headers)
    bsObj = BeautifulSoup(req.text, 'html.parser')
    (key,value,dummy)=bsObj.prettify().split('"')
    (name,open,previousClose,price,high,low,buy,sell,volume,amount,b1v,b1,b2v,b2,b3v,b3,b4v,b4,b5v,b5,s1v,s1,s2v,s3,s3v,s3,s4v,s4,s5v,s5,date,time,status)=value.split(',')
    self.name = name
    self.open = open
    self.previousClose = float(previousClose)
    self.price = price
    self.high = high
    self.low = low
    self.buy = buy
    self.sell = sell
    self.volume = volume
    self.amount = amount
    self.b1v = b1v
    self.b1 = b1
    self.b2v = b2v
    self.b2 = b2
    self.b3v = b3v
    self.b3 = b3
    self.b4v = b4v
    self.b4 = b4
    self.b5v = b5v
    self.b5 = b5
    self.s1v = s1v
    self.s1 = s1
    self.s2v = s2v
    self.s3 = s3
    self.s3v = s3v
    self.s3 = s3
    self.s4v = s4v
    self.s4 = s4
    self.s5v = s5v
    self.s5 = s5
    self.date = date
    self.time = time
    self.status = status
    self.change = (float(price)/float(previousClose)-1)*100


lines = [line.rstrip('\n') for line in open('portfolio')]
for id in lines:
  stock = instrument(id)
  stock.query()
  stock.displaySimple()
