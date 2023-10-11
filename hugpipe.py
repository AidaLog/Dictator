from transformers import VitsModel, AutoTokenizer
import torch

# initialize model
model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")

def generate(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        output = model(**inputs).waveform
    return output.float().numpy(), model.config.sampling_rate