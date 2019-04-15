import pandas as pd
import matplotlib.pyplot as plt
#from sklearn import datasets
#from sklearn.linear_model import LogisticRegression

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

##Testing LTSM
# Importing dependencies numpy and keras
import numpy
# from keras.models import Sequential
# from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils


headers = ["current", "voltage", "arc", "ref"]

data = pd.read_csv('data/data_1_cut_first_90p.txt', names=headers, sep = "\t")
data_pred = pd.read_csv('data/data_2_cut_first_90p.txt', names=headers, sep = "\t")
#data = pd.read_csv('data/data_1_cut_last_10p.txt', names=headers, sep="\t")
#data=pd.read_csv('data/data_1.txt', names=headers, skiprows=50000, sep = "\t")

feature_columns = ['current', 'voltage']

# you want all rows, and the feature_cols' columns
X = data.loc[:, feature_columns]
X_pred = data.loc[:, feature_columns]

#standardizing the input feature
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
X_pred = sc.fit_transform(X_pred)


# Create y response vector
y = data.arc

# create model
model = Sequential()
# model.add(Dense(12, input_dim=2, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

dropout = 0.2
#First Hidden Layer
model.add(Dense(128, activation='relu', kernel_initializer='random_normal', input_dim=2))
model.add(Dropout(dropout))
#Second  Hidden Layer
model.add(Dense(64, activation='relu', kernel_initializer='random_normal'))
model.add(Dropout(dropout))
#Output Layer
#model.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))
model.add(Dense(1, activation='sigmoid', kernel_initializer='lecun_normal'))

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])   # 0.9875
#model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])   # 0.9875

#model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy']) ---bad
#model.compile(optimizer=tf.keras.optimizers.SGD(lr=.05), loss='binary_crossentropy', metrics=['accuracy'])


# Fit the model
model.fit(X, y, epochs=2, batch_size=10)

model.save_weights("model/weights.h5")
model.save("model/model.h5")

# evaluate the model
# scores = model.evaluate(X, y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# calculate predictions

#predictions = model.predict(X)
predictions = model.predict(X_pred)

# round predictions
#rounded = [round(x[0]) for x in predictions]
#y_pred = [float(x[0]) for x in predictions]
#print(rounded)
y_pred = []
for x in predictions:
    if x[0] >= 0.5:
        y_pred.append(1)
    else:
        y_pred.append(0)


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
plt.plot(data.voltage, color='g')
plt.plot(y*300, color='y', linewidth=3)
plt.plot(y_pred*300, color='r', linestyle='--')

plt.legend()
plt.grid()
plt.show()
