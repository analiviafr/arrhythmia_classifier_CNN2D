# -*- coding: utf-8 -*-
"""Training_1D.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15qUOLJ6dPFBkWhDlVxXt8HFQHx0m8GKa
"""

import keras
import pandas as pd
import numpy as np
from keras.utils import np_utils
from keras import optimizers, losses, activations
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from sklearn.metrics import f1_score, accuracy_score, multilabel_confusion_matrix, confusion_matrix, precision_score, recall_score,cohen_kappa_score
from imblearn.metrics import specificity_score
import matplotlib.pyplot as plt

from VGG16 import vgg16_model

df_train = pd.read_csv('/content/drive/My Drive/analivia/ecg_signals/mitbih_train.csv', header=None)
df_test = pd.read_csv('/content/drive/My Drive/analivia/ecg_signals/mitbih_test.csv', header=None)

X_train = np.array(df_train[list(range(187))].values)[..., np.newaxis]
y_train = np.array(df_train[187].values).astype(np.int8)

X_test = np.array(df_test[list(range(187))].values)[..., np.newaxis]
y_test = np.array(df_test[187].values).astype(np.int8)

model = vgg16_model(input_shape=(187,1),n_classes=5)
opt = optimizers.Adam(lr = 0.001)
model.compile(optimizer = opt, loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

es = EarlyStopping(monitor='accuracy', mode="max", patience=5, verbose=1)
rlr = ReduceLROnPlateau(monitor='accuracy', mode="max", patience=5, verbose=2)
checkpoint = ModelCheckpoint(filepath ='pesos.h5', monitor='accuracy', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint, es, rlr]

history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs = 50, callbacks=callbacks_list)

model.load_weights('pesos.h5')

preds = model.predict(X_test)
predicted_classes = np.argmax(preds, axis = -1)

print('Matriz de Confusão')
print(multilabel_confusion_matrix(y_test, predicted_classes))

print('Matriz de Confusão')
print(confusion_matrix(y_test, predicted_classes))

print('Accuracia')
print(accuracy_score(y_test, predicted_classes))

print('Sensibilidade')
print(recall_score(y_test, predicted_classes, average='micro'))

print('Precisão')
print(precision_score(y_test, predicted_classes, average='micro'))

print('Especificidade')
print(specificity_score(y_test, predicted_classes, average='micro'))

print('F1-score')
print(f1_score(y_test, predicted_classes, average='micro')) 

gof_train_acc  = history.history['accuracy']
gof_train_loss = history.history['loss'    ]
gof_valid_acc  = history.history['val_accuracy' ]
gof_valid_loss = history.history['val_loss']
epochs = range(len(gof_train_acc))

# Graph Accuracy
plt.figure(figsize = (15,5))
plt.plot(epochs, gof_train_acc, 'b', label = 'Training')
plt.plot(epochs, gof_valid_acc, 'r', label = 'Validation')
plt.title('Accuracy')
plt.legend()
plt.show()

# Graph Loss
plt.figure(figsize = (15,5))
plt.plot(epochs, gof_train_loss, 'b', label = 'Training')
plt.plot(epochs, gof_valid_loss, 'r', label = 'Validation')
plt.title('Loss')
plt.legend()
plt.show()

# Graph Accuracy
plt.figure(figsize = (15,5))
plt.plot(epochs, gof_train_acc, 'b', label = 'Training')
plt.title('Accuracy')
plt.legend()
plt.show()

# Graph Loss
plt.figure(figsize = (15,5))
plt.plot(epochs, gof_train_loss, 'b', label = 'Training')
plt.title('Loss')
plt.legend()
plt.show()