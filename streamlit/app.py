import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
#st.markdown()
st.title("Document Title")
st.header("Article header")
st.subheader("Article subheader")
st.code("y = mx + c")
st.latex("\ int a y^2 \ , dy")
st.text("This is a chair!")
st.markdown('Staying hydrated is **_very_ cool**.')

students = ["Amelia Kami", "Antoinne Mark", "Peter Zen", "North Kim"]

marks = [82, 76, 96, 68]

import pandas as pd

df = pd.DataFrame()

df["Student Name"] = students

df["Marks"] = marks
#save to dataframe
df.to_csv("students.csv", index = False)
#display
st.dataframe(df)

#Static table
st.table(df)

#Metrics
st.metric("KPI", 56, 3)
#Json
st.json(df.to_dict())

#Code
#average of a list
code = '''def cal_average(numbers):
    sum_number = 0
    for t in numbers:
        sum_number = sum_number + t           

    average = sum_number / len(numbers)
    return average'''
st.code(code, language='python')
#progress bar

import streamlit as st
import time

# Sample Progress bar
#bar_p = st.progress(0)

#for percentage_complete in range(100):
    #time.sleep(0.1)
    #bar_p.progress(percentage_complete + 1)

#with st.spinner('Please wait...'):
    #time.sleep(5)
#st.write('Complete!')


#Displaying an image using Streamlit
from PIL import Image
image = Image.open('media/ann-savchenko-H0h_89iFsWs-unsplash.jpg')

#st.image(image, caption='Sunset grass backgrounds')

#plotly
import plotly.express as px
# This dataframe has 244 rows, but 4 unique entries for the `day` variable
df = px.data.tips()
figx = px.pie(df, values='tip', names='day', title='Tips per day')
# Plot!
st.plotly_chart(figx, use_container_width=True)

#Altair
import altair as alt
import streamlit as st
import numpy as np

df = pd.DataFrame(
     np.random.randn(300, 4),
     columns=['a', 'b', 'c', 'd'])

chrt = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c', 'd'])

st.altair_chart(chrt, use_container_width=True)

#Matplotlib
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(arr, bins=30)
plt.grid()
st.pyplot(fig)

#Interactive widgets
st.button("Click here")
#st.download_button("Download audio", file)
selected = st.checkbox("Accept terms")
choice = st.radio("Select one", ["Apples", "Oranges"])


option = st.selectbox(
     'How would you like to receive your package?',
     ('By air', 'By sea', 'By rail'))

st.write('You selected:', option)
import datetime
day = st.date_input(
     "When is your birthday?",
     datetime.date(2022, 7, 6))
st.write('Your birthday is:', day)

color = st.color_picker('Choose A Color', '#00FFAA')
st.write('The selected color is', color)


@st.cache
def fetch_data():
    df = pd.read_csv("students.csv")
    return df

#data = fetch_data()

#Visualization

import matplotlib.pyplot as plt
import numpy as np

#Matplotlib

import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
animals = ["Zebras", "Elephants", "Rhinos", "Leopards"]
number = [65, 72, 77, 59]
ax.bar(animals, number)
fig = plt.show()
st.pyplot(fig)
#Seaborn
import seaborn as sns
fig = plt.figure()
ax = sns.barplot(x = animals, y = number)
fig = plt.show()
st.pyplot(fig)

import pandas as pd
#Altair
#define data
df = pd.DataFrame()
animals = ["Zebras", "Elephants", "Rhinos", "Leopards"]
number = [65, 72, 77, 59]
df["Animals"] = animals
df["Number"] = number
#create chart
chrt = alt.Chart(df, title="Ploting using Altair in Streamlit").mark_bar().encode(
    x='Animals',
    y='Number'
)
#render with Streamlit
st.altair_chart(chrt, use_container_width=True)
#Plotly
#define data
df = pd.DataFrame()
df["Animals"] = animals
df["Number"] = number
#create plot
fig1 = px.bar(df, x='Animals', y='Number', title="Ploting using Plotly in Streamlit")
# Plot!
st.plotly_chart(fig1, use_container_width=True)

#data
df = pd.DataFrame()
df["Animals"] = animals
df["Number"] = number
#visualization
st.vega_lite_chart(df, {
     'mark': {'type': 'bar', 'tooltip': True},
     'encoding': {
         'x': {'field': 'Animals', 'type': 'nominal'},
         'y': {'field': 'Number', 'type': 'quantitative'},
     },
 }, use_container_width=True)

#Maps
import pandas as pd
states = pd.read_html('https://developers.google.com/public-data/docs/canonical/states_csv')[0]
states.columns = ['state', 'lat', 'lon', 'name']
states = states.drop(['state', 'name'], axis = 1)

st.map(states)

#Components
from st_aggrid import AgGrid
AgGrid(df)

#Statefulnness
import streamlit as st

st.title('Streamlit Counter Example')
count = 0

add = st.button('Addition')
if add:
    count += 1

st.write('Count = ', count)


import streamlit as st

st.title('Counter Session State')
if 'count' not in st.session_state:
    st.session_state.count = 0

increment = st.button('Add')
if increment:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)

#Layout
col1, col2 = st.columns(2)

with col1:
    st.altair_chart(chrt)
with col2:
    st.plotly_chart(fig1, use_container_width=True)
with st.container():
    st.plotly_chart(figx, use_container_width=True)



#Add side widget

def your_widget(key):
    st.subheader('Hi! Welcome')
    return st.button(key + "Step")

# Displayed in the main area
clicked = your_widget("First")

# Shown within an expander
your_expander = st.expander("Expand", expanded=True)
with your_expander:
    clicked = your_widget("Second")

# Shown in the st.sidebar!
with st.sidebar:
    clicked = your_widget("Last")
#Session State

#Uploading files

import streamlit as st

#upload single file
file = st.file_uploader("Please select a file to upload")
if file is not None:
    #Can be used wherever a "file-like" object is accepted:
    df= pd.read_csv(file)
    st.dataframe(df)

#Multiple files
#adding a file uploader to accept multiple CSV file
uploaded_files = st.file_uploader("Please select a CSV file", accept_multiple_files=True)
for file in uploaded_files:
    df = pd.read_csv(file)
    st.write("File uploaded:", file.name)
    st.dataframe(df)
#Uploading and Processing
#upload single file
from PIL import Image
from PIL import ImageEnhance
def load_image(image):
    img = Image.open(image)
    return img

file = st.file_uploader("Please select image to upload and process")
if file is not None:
    image = Image.open(file) 
    fig = plt.figure()
    st.subheader("Original Image")
    plt.imshow(image)
    st.pyplot(fig)
    fig = plt.figure()
    contrast = ImageEnhance.Contrast(image).enhance(12)
    plt.imshow(contrast)
    st.subheader("Preprocessed Image")
    st.pyplot(fig)

    

import streamlit as st
import streamlit as st
from transformers import pipeline

'''Hugging Face'''

import streamlit as st
from transformers import pipeline

if __name__ == "__main__":

    # Define the title of the and its description
    st.title("Answering questions using NLP through Streamlit interface")
    st.write("Pose questions, get answers")

    # Load file
    
    raw_text = st.text_area(label="Enter a text here")
    if raw_text != None and raw_text != '':

        # Display text
        with st.expander("Show question"):
            st.write(raw_text)

        # Conduct question answering using the pipeline
        question_answerer = pipeline('question-answering')

        answer = ''
        question = st.text_input('Ask a question')

        if question != '' and raw_text != '':
            answer = question_answerer({
                'question': question,
                'context': raw_text
            })

        st.write(answer)

        
        







    