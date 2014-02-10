#!/usr/bin/env python3

"""
The url is not valid any more.
"""

import urllib.request

page = urllib.request.urlopen('http://www.beans-r-us.biz/prices.html')
text = page.read().decode('utf8')

price = text[234:238]

print(price)