# sans memalign
A=[87.667,54,43.667,46,46.667,48.333,57.333]
B=[.034,.056,.069,.065,.064,.062,.052]
# avec memalign
import matplotlib.pyplot as plt
import numpy as np
A=[[6.099, 5.980, 6.129],
[5.472, 5.942, 5.457],
[6.142, 6.115, 5.777],
[5.208, 4.984, 5.364],
[5.277, 4.714, 4.807],
[4.711, 4.624, 4.830],
[4.774, 4.869, 4.787],
[3.195, 3.086, 3.121]]
Cycle = [2150.37, 1939.64, 2099.85, 1732.87, 1691.83, 1643.57, 1640.52, 1101.08]
Info = ["v0","march=\nnative","funroll-loops",
"Ofast","v1","static","restrict","v2"]
# Calculate the mean and confidence interval for each list in A
means = [np.mean(l) for l in A]
stds = [np.std(l) for l in A]
confidences_intervals = [1.96 * (std / np.sqrt(len(l))) for std, l in zip(stds, A)]
medians = [np.median(l) for l in A]
# Plot the histogram with the mean and confidence interval
fig, ax = plt.subplots()
bar = ax.bar(Info, means, yerr=confidences_intervals,capsize=4)
ax.set_xlabel("Option de compilation")
ax.set_ylabel("Temps (ms)")
# Add the median values for each bar
for i, rect in enumerate(bar):
ax.text(rect.get_x() + rect.get_width() / 2, rect.get_y() + rect.get_height() / 2,
'{:.2f}'.format(medians[i]), ha='center', va='bottom', fontsize=10)
# Add the second line plot
ax2 = ax.twinx()
ax2.plot(Info, Cycle, 'r', label='Cycles')
ax2.set_ylabel("Cycles", color='r')
ax2.tick_params(axis='y', labelcolor='r')

fig.legend()
plt.show()