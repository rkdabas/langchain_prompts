# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
# model=ChatOpenAI()
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

st.header("Research tool")

user_input = st.text_input("Enter your prompt")

if st.button('Generate'):
    result=model.invoke(user_input)
    st.write(result.content)  



