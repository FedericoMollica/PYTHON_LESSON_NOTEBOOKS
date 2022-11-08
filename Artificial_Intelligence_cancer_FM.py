#pip install tensorflow>=1.13
#pip install tensorflow


#IMPORT THE DATASET
import pandas as pd

df = pd.read_csv('cancer.csv')

x = df.drop(columns=['diagnosis(1=m, 0=b)'])
y = df['diagnosis(1=m, 0=b)']

#SPLIT THE DATA INTO A TRAINING SET AND A TESTING SET
from sklearn.model_selection import train_test_split
#modulo base per applicare AI

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2)


#BUILD AND TRAIN THE MODEL
import tensorflow as tf

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(256, input_shape=x_train.shape, activation='sigmoid'))
model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1000)
#result:
#Epoch 1000/1000
#15/15 [==============================] - 0s 3ms/step - loss: 0.0796 - accuracy: 0.9714


#EVALUATE THE MODEL 
model.evaluate(x_test, y_test)
#result:
#[0.12777677178382874, 0.9649122953414917]