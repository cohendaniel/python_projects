import urllib2
import sys
import stock

stocks = {}

def getSymbols():
	f = open('ticker_list_small.txt', 'r')
	urls = f.read().splitlines()
	print urls
	f.close()
	return urls
	
def getData(urls):
	for url in urls:
		try: 
			newStock = stock.Stock(url)
			print newStock.data
			data = urllib2.urlopen(newStock.data).read()
			data = data.split("\n")
			for line in data:
				line = line.split(',')
				if len(line) > 6 and line[0] != "Date":
					newStock.date.append(line[0])
					newStock.open.append(float(line[1]))
					newStock.high.append(float(line[2]))
					newStock.low.append(float(line[3]))
					newStock.close.append(float(line[4]))
					newStock.volume.append(float(line[5]))
					newStock.adj.append(float(line[6]))
			stocks[url] = newStock
		except:
			e = sys.exc_info()[0]
			print "Error", e;
	
symbols = getSymbols()
getData(symbols)

print stocks["GOOG"].close[0:11]
print stocks["GOOG"].EMA(9, 9, 9)