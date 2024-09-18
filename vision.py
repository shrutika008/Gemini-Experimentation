import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Load Gemini pro vision model

def get_gemini_response(input, image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit setup
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")


uploade_file = st.file_uploader("Choose an Image", type=['jpg', 'jpeg', 'png'])
image = ""
if uploade_file is not None:
    image = Image.open(uploade_file)
    st.image(image, caption="Upload Image.", use_column_width = True)

submit = st.button("Tell me about the Image")

# After Submit

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)