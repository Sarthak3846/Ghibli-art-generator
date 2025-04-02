import gradio as gr 
import requests
import os 
from PIL import Image 
from io import BytesIO

API_KEY=""
if not API_KEY:
    raise ValueError("API key is missing.")
#define the model using the variable API_URL
API_URL="https://api-inference.huggingface.co/models/   "
HEADERS = {"Authorization":f"Bearer {API_KEY}"}

def generate_ghibli_image(prompt):
    response = requests.post(API_URL,headers = HEADERS, json={"inputs":prompt})

    if response.status_code==200:
        image = Image.open(BytesIO(response.content))
        image_path = "generated_image.png"
        image.save(image_path)
        return image_path
    else:
        return f"Error: {response.json()}"
    
iface = gr.Interface(
    fn=generate_ghibli_image,
    inputs="text",
    outputs="image",  
    title="Ghibli Art Generator",
    description="Enter a text prompt and generate an AI image."
)

iface.launch()