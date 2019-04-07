#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tensorflow as tf

# load MNIST
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

print(X_train[0])
#print(y_train[0])


# convert to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# scale all input values to between 0 and 1
X_train = X_train / 255.
X_test = X_test / 255.

#print(X_train[0])
#print(y_train[0])

# define our model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),                          # 28x28 -> 784x1
    tf.keras.layers.Dense(512, activation=tf.nn.relu),  # 784x1 -> 512x1
    tf.keras.layers.Dense(10, activation=tf.nn.softmax) # 512x1 -> 10x1
])

# define our optimizer and loss function
model.compile(optimizer=tf.keras.optimizers.SGD(lr=.05), loss='categorical_crossentropy', metrics=['accuracy'])

# train our model!
model.fit(X_train, y_train, epochs=5, callbacks=[tf.keras.callbacks.TensorBoard(log_dir='deeper_mnist')])

# compute the accuracy for the test set
loss, accuracy = model.evaluate(X_test, y_test)
print('{:.4}'.format(accuracy))
