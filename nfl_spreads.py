# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 9 Assignment, Part 2

import urllib2
from bs4 import BeautifulSoup

url = "http://www.footballlocks.com/nfl_point_spreads_week_4.shtml"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
#print soup.prettify()

nflspread = soup.find_all("table", attrs={"border":"0", "cellpadding":"4", "cellspacing":"8", "cols":"4", "width":"562"})[0]
#print(nflspread)
nfltrs = nflspread.find_all('tr')
#print(nfltrs)

Ranking = 0
for tr in nfltrs:
    if Ranking > 0:
        i=0
        Date = None
        Favorite = None
        Spread = None
        Underdog = None
        for td in tr:
            if i == 1:
                Date = td.get_text()
            if i == 3:
                Favorite= td.get_text()
            if i == 5:
                Spread = td.get_text().strip()
            if i == 7:
                Underdog = td.get_text()
            i= i+1
        print("Date: {}, Favorite: {}, Spread:{}, Underdog:{}".format(Date, Favorite, Spread, Underdog))
    Ranking = Ranking + 1
