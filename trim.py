import datatools as dt
import pyperclip

data = dt.DataProcessor(pyperclip.paste()).convert().get()

for i in range(len(data)):
    try:
        if (data[i+1]-data[i] <= 0) and (data[i+1] <= data[0]):
            # in order for a point to be considered the lowest point at the start of the increase in co2, it must be a decrease or no change from the previous point and less than the starting point
            print("decrease or no change at index: " + str(i) + " value: " + str(data[i]) + " row: " + str(i + 3) + " could be a good starting point.")
    except:
        print("exception: done")
