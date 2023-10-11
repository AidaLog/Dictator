from transformers import VitsModel, AutoTokenizer
import torch

# initialize model
model = VitsModel.from_pretrained("facebook/mms-tts-eng")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-eng")