import numpy as np
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

#dataset = pd.read_csv('data/data_1_cut_first_90p.csv')
dataset = pd.read_csv('data/data_1_cut_last_10p.csv')

X= dataset.iloc[:, 0:2]  # Select first 2 columns - current and voltage, all rows
y= dataset.iloc[:,2]    # Select arc

#standardizing the input feature
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from keras import Sequential
from keras.layers import Dense

classifier = Sequential()
#First Hidden Layer
classifier.add(Dense(4, activation='relu', kernel_initializer='random_normal', input_dim=2))

#Second  Hidden Layer
classifier.add(Dense(4, activation='relu', kernel_initializer='random_normal'))

#Output Layer
classifier.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))

#Compiling the neural network
classifier.compile(optimizer = 'adam', loss='binary_crossentropy', metrics =['accuracy'])

#Fitting the data to the training dataset
#classifier.fit(X_train, y_train, batch_size=10, epochs=5)
classifier.fit(X, y, batch_size=10, epochs=10)

# Evaluate the loss value & metrics values for the model in test mode using evaluate function
# eval_model=classifier.evaluate(X_train, y_train)
# print(eval_model)

# Predict the output for our test dataset. If the prediction is greater than 0.5 then the output is 1 else the output is 0
# y_pred = classifier.predict(X_test)
# y_pred = (y_pred>0.5)

# # Check the accuracy on the test dataset
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, y_pred)
# print(cm)


#Test the predictor
dataset2 = pd.read_csv('data/data_2_cut_last_10p.csv')

X2 = dataset.iloc[:, 0:2]  # Select first 2 columns - current and voltage, all rows
y2 = dataset.iloc[:,2]    # Select arc

#standardizing the input feature
sc2 = StandardScaler()
X2 = sc2.fit_transform(X)

# y_pred = classifier.predict(X2)
# y_pred = (y_pred>0.5)

# calculate predictions
predictions = classifier.predict(X2)
# round predictions
rounded = [round(x[0]) for x in predictions]
#print(rounded)

with open('data/prediction_1.csv', "w") as outfile:
    for x in rounded:
        line = "{}\n".format(x)
        outfile.write(line)

headers = ['arc_pred']
data_pred = pd.read_csv('data/prediction_1.csv', names=headers)

#data_combined = pd.merge(data, data_pred)
#data2 = data[["voltage", "arc"]]
data2 = data.arc
data3 = data_pred.arc_pred

data2.plot()
data3.plot()
plt.show()
