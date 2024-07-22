from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image



os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
   
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Code Helper")

## Code Generator
st.header("Search for code")
prewritten_text = "Give code for the"
input=st.text_input("Enter the question")
input1=st.text_input("Enter the language")
combined_text =f"{prewritten_text}  ,{input} ,{input1}"

submit=st.button("Get Code")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(combined_text)
    st.subheader("Code is:")
    st.write(response)

# ## Code Translator
st.header("Code Translator")

text="Convert this code into "
codeInput=st.text_input("Enter your Code: ")
codeInput1=st.text_input("Enter language in which you want to convert")

comtext=f"{codeInput} ,{text},{codeInput1}"

submitbtn=st.button("Convert Code")

if submitbtn:
    
    response=get_gemini_response(comtext)
    st.subheader("The Response is")
    st.write(response)

## Error debugger

st.header("Error Debugger")

text="Resolve this error step by step"
codeInput=st.text_input("Enter your error : ")
comtext=f"{codeInput} ,{text}"

submitbtn=st.button("Resolve Error")

if submitbtn:
    response=get_gemini_response(comtext)
    st.subheader("The Response is")
    st.write(response)

## image code generator
model = genai.GenerativeModel('gemini-1.5-flash')
textinp="Generate code in java"
def get_gemini_response(textinp,image):
    
    if textinp!="":
       response = model.generate_content([textinp,image])
    else:
       response = model.generate_content(image)
    return response.text

st.header("Upload Image for code")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Get code")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(textinp,image)
    st.subheader("The Response is")
    st.write(response)


