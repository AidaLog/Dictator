from hugpipe import *
import streamlit as st



st.title("Text to Speech App with Transformers")

# Input text
input_text = st.text_area("Enter text for conversion")

# Button to convert text to speech
if st.button("Convert to Speech"):
    if input_text:
        # Generate audio
        output, rate = generate(input_text)
        st.audio(output, format="audio/wav", sample_rate=rate)
        # Download audio file
        st.success("File ready to play and download")

    else:
        st.warning("Please enter some text before converting.")