import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the csv file
df = pd.read_csv('Chinas GDP in Province.csv')

# x1 is array of quantile of GDP Beijing
# x2 is array of quantile of GDP Shanghai
x1 = df['Beijing'].quantile(np.linspace(0, 1, 67))
x2 = df['Shanghai'].quantile(np.linspace(0, 1, 67))

# plot scatter of x1 and x2
plt.scatter(x1, x2)
# plot line of x1 quantiles
plt.plot([min(x1), max(x1)], [min(x1), max(x1)], color="red")

# plot title, x-label, and y-label
plt.title('QQ Plots of Gross Domestic Product\nBeijing & Shanghai',
          fontsize=13, fontweight='bold', pad=10)
plt.xlabel("Beijing")
plt.ylabel("Shanghai")

# Save the QQ plot to a PNG file
plt.savefig('qq_plot.png')

# show the plot
plt.show()
