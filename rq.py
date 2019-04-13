#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup


class instrument:

    def __init__(self, id):
        self.id = id

    def displaySimple(self):
        print ('{:^8} {:8.2f} {:6.2f}%'.format(self.id, self.price, self.change))

    def displayDetail(self):
        print ('{:^8} {:^8} {:8.2f} {:6.2f}%'.format(self.id, self.name, self.price, self.change))
        #print ('{:8.2f} {:12.0f} '.format(self.s5p, self.s5v))
        #print ('{:8.2f} {:12.0f} '.format(self.s4p, self.s4v))
        #print ('{:8.2f} {:12.0f} '.format(self.s3p, self.s3v))
        #print ('{:8.2f} {:12.0f} '.format(self.s2p, self.s2v))
        #print ('{:8.2f} {:12.0f} '.format(self.s1p, self.s1v))
        #print ()
        #print ('{:8.2f} {:12.0f} '.format(self.b1p, self.b1v))
        #print ('{:8.2f} {:12.0f} '.format(self.b2p, self.b2v))
        #print ('{:8.2f} {:12.0f} '.format(self.b3p, self.b3v))
        #print ('{:8.2f} {:12.0f} '.format(self.b4p, self.b4v))
        #print ('{:8.2f} {:12.0f} '.format(self.b5p, self.b5v))

    def query(self):
        session = requests.session()
        headers = {"User-Agent": "Chrome", "Accept":"text/html, application/xhtml+xml, application/xml; q=0.9, image/webp, */*; q=0.8"}
        url = "http://hq.sinajs.cn/list=" + self.id
        req = session.get (url, headers=headers)
        bsObj = BeautifulSoup(req.text, 'html.parser')
        (key,value,dummy)=bsObj.prettify().split('"')
        (name,open,previousClose,price,high,low,buy,sell,volume,amount,b1v,b1p,b2v,b2p,b3v,b3p,b4v,b4p,b5v,b5p,s1v,s1p,s2v,s2p,s3v,s3p,s4v,s4p,s5v,s5p,date,time,status)=value.split(',')
        self.name = name
        self.open = open
        self.previousClose = float(previousClose)
        self.price = float(price)
        self.high = high
        self.low = low
        self.buy = buy
        self.sell = sell
        self.volume = volume
        self.amount = amount
        self.b1v = float(b1v)
        self.b1p = float(b1p)
        self.b2v = float(b2v)
        self.b2p = float(b2p)
        self.b3v = float(b3v)
        self.b3p = float(b3p)
        self.b4v = float(b4v)
        self.b4p = float(b4p)
        self.b5v = float(b5v)
        self.b5p = float(b5p)
        self.s1v = float(s1v)
        self.s1p = float(s1p)
        self.s2v = float(s2v)
        self.s2p = float(s3p)
        self.s3v = float(s3v)
        self.s3p = float(s3p)
        self.s4v = float(s4v)
        self.s4p = float(s4p)
        self.s5v = float(s5v)
        self.s5p = float(s5p)
        self.date = date
        self.time = time
        self.status = status
        self.change = (float(price)/float(previousClose)-1)*100

def main(*args):
    if len(args) == 0:
        lines = [line.rstrip('\n') for line in open('portfolio')]
        for id in lines:
            stock = instrument(id)
            stock.query()
            stock.displaySimple()
    else:
        for id in args:
            stock = instrument(id)
            stock.query()
            stock.displayDetail()

if __name__== "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
