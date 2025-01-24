class DataProcessor: #this class contains the main functions I use to process individual lists
	def __init__(self, list):
		self.list = list 
	def convert(self):
		self.list = self.list.replace("\n"," ").split() #Convert google sheets / desmos clipboard data to python usable form
		flist = []
		for i in range(len(self.list)):
			flist.append(float(self.list[i]))
		self.list = flist
		return self
	def unconvert(self): #Convert python data back to google sheets / desmos usable form
		slist = []
		for i in range(len(self.list)):
			slist.append(str(self.list[i]))
		clist = '\n'.join(slist)
		self.list = clist
		return self
	def reduceSecondIntervals(self):
		#Needed because some probes procude data points corresponding to 4 seconds, and others 2
		#Accuracy is limited by the 4 second probes
		hlist = []
		for i in range(len(self.list)):
			if i % 2 == 0:
				hlist.append(self.list[i])
		self.list = hlist
		return self
	def get(self):
		return self.list

class ApproxDerivative:
	def __init__(self, xList, yList):
		self.xList = xList
		self.yList = yList
	def get(self):
		xDerivativeList = []
		for i in range(len(self.yList) - 1):
			deltaX = self.xList[i+1] - self.xList[i] #dx
			deltaY = self.yList[i+1] - self.yList[i] #dy
			xDerivativeList.append(deltaY / deltaX) #dy/dx
		return xDerivativeList
