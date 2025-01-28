import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xAxis = ['0.5', '1.0', '2.0', '4.0', '8.0']
yAxis = [12.646038, 20, 20, 20, 33.395914]

bar_labels = ['red', 'blue', 'yellow', 'orange', 'purple']
bar_colors = ['tab:red', 'tab:blue', 'tab:olive', 'tab:orange', 'tab:purple']

ax.bar(xAxis, yAxis, color=bar_colors)

ax.set_xlabel('Sucrose / g')
ax.set_ylabel('Average rate of CO2 Uptake / ppm * sec^-1')
ax.set_title('Average rate of CO2 uptake for a given amount of sucrose, \nerror bars represent second standard deviation.')

#ax.legend(title='Fruit color')

errors = [3.063846976, 2, 3, 4, 13.76148297]

plt.errorbar(xAxis, yAxis, yerr=errors, fmt="o", color="r")

plt.show()
