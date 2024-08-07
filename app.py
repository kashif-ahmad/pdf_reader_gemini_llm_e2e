from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from definitions import *

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## initialize streamlit app

st.set_page_config(page_title="Invoice Reader - Google Gemini")
st.header("Invoice Reader - Google Gemini")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image="" 

if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the Invoice")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

# if submit button is clicked
if submit:
   image_data = input_image_details(uploaded_file)
   response=get_gemini_response(input_prompt,image_data,input)
   st.subheader("The Response is")
   st.write(response)


