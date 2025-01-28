import datatools as dt
import data
import pyperclip

xList = dt.DataProcessor(data.time_1).reduceSecondIntervals().get()
yList = dt.DataProcessor(data.co2_1).reduceSecondIntervals().get()

dataSet = dt.XYData(xList, yList)

dataSet.calcDerivative()

print(dataSet.getXList())
print(dataSet.getDerivativeList())

#pyperclip.copy(output.reduceSecondIntervals().unconvert().list)


