import pandas as pd
import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.linear_model import LogisticRegression

from keras.models import Sequential
from keras.layers import Dense


headers = ["current", "voltage", "arc", "ref"]

data = pd.read_csv('data/data_1_cut_first_90p.txt', names=headers, sep = "\t")
data_pred = pd.read_csv('data/data_2_cut_first_90p.txt', names=headers, sep = "\t")
#data = pd.read_csv('data/data_1_cut_last_10p.txt', names=headers, sep="\t")
#data=pd.read_csv('data/data_1.txt', names=headers, skiprows=50000, sep = "\t")

feature_columns = ['current', 'voltage', 'ref']

# you want all rows, and the feature_cols' columns
X = data.loc[:, feature_columns]
X_pred = data.loc[:, feature_columns]
print(X.shape)

#standardizing the input feature
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
X_pred = sc.fit_transform(X_pred)


# Create y response vector
y = data.arc
print(y.shape)


# create model
model = Sequential()
# model.add(Dense(12, input_dim=2, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

#First Hidden Layer
model.add(Dense(16, activation='relu', kernel_initializer='random_normal', input_dim=3))
#Second  Hidden Layer
model.add(Dense(8, activation='relu', kernel_initializer='random_normal'))
#Third  Hidden Layer
model.add(Dense(4, activation='relu', kernel_initializer='random_normal'))
#Output Layer
model.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(X, y, epochs=2, batch_size=20)

# evaluate the model
# scores = model.evaluate(X, y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# calculate predictions
#predictions = model.predict(X)
predictions = model.predict(X_pred)

# round predictions
rounded = [round(x[0]) for x in predictions]
#print(rounded)

# with open('data/prediction_1.csv', "w") as outfile:
#     for x in rounded:
#         line = "{}\n".format(x)
#         outfile.write(line)

# headers = ['arc_pred']
# data_pred = pd.read_csv('data/prediction_1.csv', names=headers)

# #data_combined = pd.merge(data, data_pred)
# #data2 = data[["voltage", "arc"]]
# data2 = data.arc
# data3 = data_pred.arc_pred

linestyles = ['-', '--', '-.', ':']
# data2.plot('g')
# data3.plot('r')
plt.plot(y, color='g', linewidth=3)
plt.plot(rounded, color='r', linestyle=':')
plt.show()
