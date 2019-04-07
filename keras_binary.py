import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout


import math

def extract_data_lists(lines):

    current_list = []
    voltage_list = []
    arc_list = []
    ref_current_list = []

    idx_tuples = []
    short = False
    start = 0

    for line in lines:
        x = line.strip()
        current, voltage, isShort, reference = x.split()

        current_list.append(int(current))
        voltage_list.append(int(voltage))
        #arc_list.append(int(isShort)*300)
        arc_list.append(int(isShort))
        ref_current_list.append(int(reference))

        if int(isShort) == 1:
            short = True
            if start == 0:
                start = lines.index(line)
                #print('Got START idx: {}'.format(start))
        else:
            if short:
                end = lines.index(line)
                #print('Got END idx: {}'.format(end))
                #print('Sample len idx: {}'.format(end-start))

                idx_tuples.append((start, end))
                short = False
                start = 0
            else:
                pass

    return current_list, voltage_list, arc_list, ref_current_list, idx_tuples


fname_list = [
    'data/data_1.txt',
    'data/data_2.txt',
    'data/data_3.txt',
    'data/data_4.txt']

fname_list_mod = [
    'data/data_1_cut_last_10p.txt',
    'data/data_2_cut_last_10p.txt',
    'data/data_3_cut_last_10p.txt',
    'data/data_4_cut_last_10p.txt']


## Open data file
with open(fname_list_mod[0]) as f:
    content = f.readlines()

current_list, voltage_list, arc_list, ref_current_list, idx_tuples = extract_data_lists(content)

x_train = voltage_list[:239200]
y_train = arc_list[:239200]

#np.hstack(zip(A,B))
list(zip(current_list, voltage_list))

#x_test = voltage_list[239201:]
x_test = list(zip(current_list[239201:], voltage_list[239201:]))
y_test = arc_list[239201:]

# convert to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

model = Sequential()
model.add(Dense(64, input_dim=1, activation='relu'))
model.add(Dropout(0.5))
# model.add(Dense(64, activation='relu'))
# model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=2,
          batch_size=128,
          callbacks=[tf.keras.callbacks.TensorBoard(log_dir='keras_binary')])

score = model.evaluate(x_test, y_test, batch_size=128)
