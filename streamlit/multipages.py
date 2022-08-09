import streamlit as st

def main_page():
    #Matplotlib
    st.set_option('deprecation.showPyplotGlobalUse', False)
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

    st.sidebar.markdown("Seaborn and Matplotlib")

def page2():
    import pandas as pd
    import altair as alt
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
    st.sidebar.markdown("Altair")

def page3():
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
    st.sidebar.markdown("Students info")

page_names_to_funcs = {
    "Seaborn and Matplotlib": main_page,
    "Altair": page2,
    "Data table": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()