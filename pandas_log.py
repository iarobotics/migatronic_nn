import pandas as pd
import matplotlib.pyplot as plt


headers = ["current", "voltage", "arc", "ref"]

data=pd.read_csv('data/data_1.txt', names=headers, skiprows=50000, sep = "\t")

# %Y - year including the century
# %m - month (01 to 12)
# %d - day of the month (01 to 31)
#data['Date']=pd.to_datetime(data['Date'], format="%Y/%m/%d")

print(data.head(2))

data2 = data[["voltage", "arc"]]

data2.plot()
plt.show()
