import matplotlib.pyplot as plt

fig, ax = plt.subplots()

xAxis = [0.5, 1.0, 2.0, 4.0, 8.0]
yAxis = [11.270115, 18.586385, 29.09563833, 28.27753, 33.166978]
errors = [0.7305563665, 2.440473784, 4.31619669, 7.185158406, 7.435532497]

bar_labels = ['red', 'blue', 'yellow', 'orange', 'purple']
bar_colors = ['tab:red', 'tab:blue', 'tab:olive', 'tab:orange', 'tab:purple']

#ax.bar(xAxis, yAxis, color=bar_colors)

ax.set_xlabel('Sucrose / g')
ax.set_ylabel('Average rate of CO2 Uptake / ppm * sec^-1')
ax.set_title('Figure 2: Average rate of CO2 uptake for a given amount of sucrose.\nY axis represents mass of sucrose added to 100mL of water.\nX axis represents the average slope of the linear regression of each trial at a certain mass of sucrose.\nError bars represent standard error.')

#ax.legend(title='Fruit color')

plt.errorbar(xAxis, yAxis, yerr=errors, fmt="o", color="r")

plt.plot(xAxis, yAxis)

plt.show()
