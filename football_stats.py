# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 9 Assignment, Part 1

import urllib2
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
#print soup.prettify()

nfltable = soup.find_all("table", attrs={"class":"data"})[0]
#print(nfltable)
nfltrs = nfltable.find_all('tr', attrs={"valign":"top"})

Ranking = 1
for tr in nfltrs:
    if Ranking <=20:
        i=0
        Player = None
        Position = None
        Team = None
        Touchdowns = None
        for td in tr:
            if i == 0:
                Player = td.get_text()
            if i == 1:
                Position= td.get_text()
            if i == 2:
                Team = td.get_text()
            if i == 6:
                Touchdowns = td.get_text()
            i= i+1
        print("Ranking: {}, Player Name: {}, Position: {}, Team: {}, Total Touchdowns: {}".format(Ranking, Player, Position, Team, Touchdowns))
    Ranking = Ranking + 1
