__author__ = 'ronfe'

import string, urllib2, re

def initInfo():
    goalPrice = raw_input('Please enter the goal price: ')
    sltStocks = raw_input('Please enter the number ')
    sltStocks = string.atoi(sltStocks)

    priceString = '，股价低于'.decode('utf-8') + goalPrice
    defaultQuery = '市值小于100亿，股本小于10亿，市盈率小于50，近三年都盈利，股价高于60日均线'.decode('utf-8') + priceString

    return defaultQuery.encode('utf-8')

def main():
    query = initInfo()
    url = 'http://www.iwencai.com/stockpick/search?typed=0&preParams=&ts=1&f=1&qs=1&selfsectsn=&querytype=&searchfilter=&tid=stockpick&w=' + query
    f = urllib2.urlopen(url).readlines()
    f = ''.join(f)
    # find stock codes by id
    stocks = re.findall(r'<div class="em alignCenter" >\d+</div>', f)
    stripped_stocks = []
    if len(stocks) >= 1:
        # strip tags
        for each in stocks:
            temp = re.sub(r'<.+?>', '', each)
            stripped_stocks.append(temp)
        print stripped_stocks
    else:
        print 'No results!'
        return 0

main()


