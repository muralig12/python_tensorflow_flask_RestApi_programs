# Convolutional Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import cv2


# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

classifier.fit_generator(training_set,
                         samples_per_epoch = 8000,
                         nb_epoch = 5,
                         validation_data = test_set,
                         nb_val_samples = 2000)

img = cv2.imread("./dataset/dog.jpg")
img = cv2.resize(img, (64,64))
print(img.shape)
img = img.reshape(1, 64, 64, 3)

print(img.shape)
#print(np.argmax(loaded_model.predict(img)))
print(classifier.predict(img))
result=classifier.predict(img)
if result[0][0]==1:
    print("dog")
else:
    print("cat")
    
#saving keras model
#from keras.models import load_model
classifier.save('my_model.h5')


##Save model to json
import os
from keras.models import model_from_json

clssf = classifier.to_json()
with open("CatOrDog.json", "w") as json_file:
    json_file.write(clssf)
classifier.save_weights("CorDweights.h5")
print("model saved to disk....")


"""

# save keras model

from keras.models import load_model
classifier.save('my_model.h5')
model = load_model('my_model.h5')

#loading Keras model in another program

from keras.models import load_model
model = load_model('my_model.h5')

import cv2
from keras.applications.imagenet_utils import preprocess_input, decode_predictions

img = cv2.imread("./dataset/cat2.jpeg")
img = cv2.resize(img, (64,64))
print(img.shape)
img = img.reshape(1, 64, 64, 3)

print(img.shape)
#print(np.argmax(loaded_model.predict(img)))
print(model.predict(img))
result=model.predict(img)
if result[0][0]==1:
    print("its a Dog")
else:
    print("its a Cat")

"""