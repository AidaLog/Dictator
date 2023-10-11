from transformers import VitsModel, AutoTokenizer
import torch
from IPython.display import Audio
import streamlit as st

# initialize model
model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")


st.title("Text to Speech App with Transformers")

# Input text
input_text = st.text_area("Enter text for conversion")

# Button to convert text to speech
if st.button("Convert to Speech"):
    if input_text:
        inputs = tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            output = model(**inputs).waveform

            # Play audio
        st.audio(audio.numpy(), format="audio/wav")
    else:
        st.warning("Please enter some text before converting.")