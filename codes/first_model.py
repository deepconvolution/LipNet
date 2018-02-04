

import numpy as np
from keras.models import Sequential # To initialise the nn as a sequence of layers
from keras.layers import Convolution2D # To make the convolution layer for 2D images
from keras.layers import MaxPooling2D # 
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.callbacks import CSVLogger
from keras.optimizers import RMSprop
from keras.layers import BatchNormalization
from keras.optimizers import Adam
from keras.models import load_model
from keras.callbacks import ModelCheckpoint

csv=CSVLogger("First_model.log")
filepath="weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')


# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32,(2,2),input_shape = (224,224,1), activation = 'relu',strides=2,name='convo1'))
classifier.add(Convolution2D(64,(3,3), activation = 'relu',name='convo2'))
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2,2)))

# Step 1 - Convolution
classifier.add(Convolution2D(64,(3,3),activation = 'relu',name='convo3'))
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2,2)))
# Step 3 - Flattening
classifier.add(Convolution2D(64,(3,3),activation = 'relu',name='convo4'))
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2,2)))



classifier.add(Flatten())
classifier.add(BatchNormalization())
classifier.add(Dropout((0.5)))
classifier.add(Dense(1024, activation = 'relu'))
classifier.add(BatchNormalization())
classifier.add(Dropout((0.4)))
classifier.add(Dense(20, activation = 'softmax'))



classifier.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory('Train',target_size=(224, 224),batch_size=32,class_mode='categorical')

test_set = test_datagen.flow_from_directory('Test',target_size=(224, 224),batch_size=32,class_mode='categorical')

history = classifier.fit_generator(train_set,steps_per_epoch=47605,epochs=5,validation_data=test_set,validation_steps=12921,callbacks=[csv,checkpoint])

