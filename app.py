### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("G_API_KEY"))

## Function to load Google Gemini Pro Vision API And get response

def get_gemini_repsonse(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app

st.set_page_config(page_title="Your Food Doctor")

st.header("Your Food Doctor")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell Me About This Food")

input_prompt="""
Firstly check the given image is of food or not if not then directly said "This is not Appropriate Image Please upload another image.
As a nutrition expert, you would like to analyze the food items in the given image and provide a detailed report on their calorie,
 Carbohydrates, Proteins, Lipids (Fats), Water, Minerals, Vitamins content. 
Additionally, you will provide a breakdown of the  content of each food item in the following format:
Item 1 - 
Item 2 - 
...
n. Item n - 
Furthermore, you will provide an expert opinion on the overall healthiness of the food items in the image.
 Based on the calorie, calorie,
 Carbohydrates, Proteins, Lipids (Fats), Water, Minerals, Vitamins content. content and nutritional value of the food items, I will provide a detailed explanation of whether the food is healthy or unhealthy. My analysis will be based on current scientific research and guidelines from reputable health organizations.

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_repsonse(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)

