import datatools as dt
import data
import pyperclip

xList = data.time_1
yList = data.co2_1


D1 = dt.ApproxDerivative(xList, yList)


output = dt.DataProcessor(D1.get())

print("data copied to clipboard")

pyperclip.copy(output.reduceSecondIntervals().unconvert().list)


