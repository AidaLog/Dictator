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
        inputs = tokenizer(input_text, return_tensors="pt")

        with torch.no_grad():
            output = model(**inputs).waveform

        # Display audio using IPython's Audio widget
        audio_display = Audio(data=output.numpy(), rate=model.config.sampling_rate)
        st.write(audio_display)

    else:
        st.warning("Please enter some text before converting.")