from hugpipe import *
import streamlit as st



st.title("👴 HugPipe Text Dictator 🎙")

# Input text
input_text = st.text_area("Enter text for conversion")

# Button to convert text to speech
if st.button("Convert to Speech"):
    if input_text:
        # Generate audio
        try:
            output, rate = generate(input_text)
            st.audio(output, format="audio/wav", sample_rate=rate)
            # Download audio file
            st.success("File ready to play and download")
        except:
            st.error("Sorry, something went wrong. Please reload the page.")

    else:
        st.warning("Please enter some text before converting.")