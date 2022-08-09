import PIL
print('Pillow Version:', PIL.__version__)

from PIL import Image

from matplotlib import image
from matplotlib import pyplot
import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import os
import tensorflow as tf
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2
from tensorflow import keras
from tensorflow.keras.models import Sequential, Model
from  matplotlib import pyplot as plt
import matplotlib.image as mpimg
import random
%matplotlib inline

#generate dataset
IMG_WIDTH=200
IMG_HEIGHT=200
img_path='train'
#generate dataset
IMG_WIDTH=200
IMG_HEIGHT=200
img_path='train1/'
def generate_dataset(img_path):
    img_data_array=[]
    class_name=[]
    for file in os.listdir(os.path.join(img_path)):
        image = cv2.imread( img_path+file, cv2.COLOR_BGR2RGB)
        try:
            image = cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH),interpolation = cv2.INTER_AREA)
        except:
            break
        image = np.array(image)
        image = image.astype('float32')
        image /= 255 
        img_data_array.append(image)
        # determine class
        output = 0
        if file.startswith('dog'):
            output = 1
        class_name.append(output)
    return img_data_array, class_name
# Get the image array and class name
img_data, class_name = generate_dataset(img_path)

'''Convert to array'''
img_data=np.array(img_data)
class_name=np.array(class_name)
img_data.shape
'''Dog mapping'''
def dog_cat_mapping(a):
    if a=="dogs":
        return 1
    else:return 0
class_name=list(map(dog_cat_mapping,class_name))
class_name=np.array(class_name)
#input shape for model parameters
input_shape=img_data.shape[1:]
'''Modeling'''
from tensorflow.keras.applications import InceptionResNetV2
conv_base=InceptionResNetV2(weights='imagenet',include_top=False,input_shape=(200,200,3))
#Define the model
def model():
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
    model=Sequential()
    model.add(conv_base)
    model.add(Flatten())
    model.add(Dense(256,activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1,activation='sigmoid'))
    return model
model = model()
#check structure
#model.summary()
conv_base.trainable = False
#compile the model
model.compile(optimizer = 'adam', 
              loss = 'binary_crossentropy', 
              metrics = ['accuracy'])
model.fit(x = img_data,y = class_name, epochs = 2)
#save the model
model.save('catdog.h5', save_format='tf')
