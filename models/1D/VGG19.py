# -*- coding: utf-8 -*-
"""VGG19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXWJz5WWXBS46GsmPJMsmMQnuinI7sup
"""

from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout

def vgg19_model(input_shape, n_classes):
  model = Sequential()
  model.add(Conv1D(64, input_shape=input_shape, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(64, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(MaxPooling1D(pool_size=2, strides=2, padding='same'))

  model.add(Conv1D(128, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(128, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(MaxPooling1D(pool_size=2, strides=2, padding='same'))

  model.add(Conv1D(256, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(256, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(256, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(256, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(MaxPooling1D(pool_size=2, strides=2, padding='same'))

  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(MaxPooling1D(pool_size=2, strides=2, padding='same'))

  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(Conv1D(512, kernel_size=3, strides=1, activation='relu', padding='same'))
  model.add(MaxPooling1D(pool_size=2, strides=2, padding='same'))

  model.add(Flatten())
  model.add(Dense(4096, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(4096, activation='relu'))
  model.add(Dropout(0.5))
  model.add(Dense(n_classes, activation='softmax'))  
  
  return model

if __name__ == '__main__':
  model = vgg19_model(input_shape=(187,1), n_classes=5)
