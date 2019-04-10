import pandas as pd
import matplotlib.pyplot as plt


headers = ["current", "voltage", "arc", "ref"]
headers_mod = ["current", "voltage", "arc_mod", "ref"]

data_mod = pd.read_csv('data/data_1_cut_first_90p.txt', names=headers_mod, sep = "\t")
data = pd.read_csv('data/data_1.txt', names=headers, sep = "\t", skiprows=50000)

feature_columns = ['current', 'voltage']

# you want all rows, and the feature_cols' columns
X = data.loc[:, feature_columns]
X_mod = data_mod.loc[:, feature_columns]

arc_mod = data_mod.arc_mod
arc = data.arc

# print(X.shape)
# print(X_mod.shape)
# print(arc.shape)
# print(arc_mod.shape)

linestyles = ['-', '--', '-.', ':']
# data2.plot('g')
# data3.plot('r')
#plt.plot(data.current, color='b', linewidth=3)
#plt.plot(data.current - 1000, color='b')
plt.plot(data.voltage, color='g')
plt.plot(arc*300, color='y', linewidth=3)
plt.plot(arc_mod*300, color='r', linestyle='--')
plt.legend()
plt.grid()
plt.show()
