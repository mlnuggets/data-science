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
