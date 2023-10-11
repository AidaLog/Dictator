from hugpipe import *
import streamlit as st



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
        st.audio(output.float().numpy(), sample_rate=model.config.sampling_rate)

        # Download audio file
        st.success("File ready to play and download")

    else:
        st.warning("Please enter some text before converting.")