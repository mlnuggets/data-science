import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

st.title("Cat/Dog Streamlit Classifier")
st.header("Please input an image to be classified:")

@st.cache(allow_output_mutation=True)

def dog_cat_classifier(img, model):
    '''
    Teachable machine learning classifier for dog-cat classification:
    Parameters
    {
    img: Image to be classified
    model : trained model
    
    }
    '''
    # Load the model that was saved earlier
    model = keras.models.load_model(model)

    '''Define the array of the right shape to feed into the keras model'''
    
    data = np.ndarray(shape=(1, 200, 200, 3), dtype=np.float32)
    image = img
    #resizing the image
    size = (200, 200)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #convert the image into a numpy array
    image_array = np.asarray(image)
    # Image processing (normalization)
    normalized_image = (image_array.astype(np.float32) / 255)

    # Load the image into the array
    data[0] = normalized_image

    # carryout predictions
    prediction_rate = model.predict(data)
    
    prediction = prediction_rate.round()
    
    return  prediction, prediction_rate

#prompt user for an image
uploaded_image = st.file_uploader("Select an image with Cat or Dog Image...", type="jpg")

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded file', use_column_width=True)
    st.write("")
    st.write("Classifying please wait...")
    label, conf = dog_cat_classifier(image, 'catdog.h5')
    if label == 1:
        st.write("This is a Dog, with:",conf, "confidence")
    else:
        st.write("This is a Cat, with:",1-conf, "confidence")
