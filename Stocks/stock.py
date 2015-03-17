class Stock:
	def __init__(self, name):
		self.date = []
		self.open = []
		self.high = []
		self.low = []
		self.close = []
		self.volume = []
		self.adj = []
		self.data = "http://real-chart.finance.yahoo.com/table.csv?s="+name+"&d=11&e=29&f=2014&g=d&a=3&b=12&c=1996&ignore=.csv"
	
	#Let start be the most recent day, and the length be the number of
	#days back in history to measure
	def SMA(self, start, length):
		if start - length < 0:
			print "Range out of bounds"
			return
		else:
			print sum(self.close[start - length:start])/length
			return
	
	def EMA(self, start, length, period):
		a = 2.0/(period+1)
		if start - length < 0:
			print "Range out of bounds"
			return
		elif length == 0:
			return self.close[start-period]
		else:
			return (a*self.close[start-period+length-1]) + ((1-a)*self.EMA(start, length-1, period))
			
	def MACD(self, start, low, high, signal):
		print "Implement MACD"
		
		