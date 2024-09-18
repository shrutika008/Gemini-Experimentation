from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Gemini Model

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(upload_file):
    if upload_file is not None:
        bytes_data = upload_file.getvalue()

        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file Uploaded")

#Streamlt set up
st.set_page_config(page_title="Multilanguage Invoice Extractor")
st.header("Multilanguage Invoice Extractor")
input = st.text_input("Input Prompt: ", key="input")

upload_file = st.file_uploader("Choose an Invoice Image", type=['jgp', 'png', 'jpeg'])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Upload Image", use_column_width=True)

submit = st.button("Tell me about Invoice")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
              """

if submit:
    image_data = input_image_setup(upload_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)