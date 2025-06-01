#  Now we are using the prompt template from the json file, that is the code is reusable now.
# We have load the same prompt template to multiple files, using load_prompt()

# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
# model=ChatOpenAI()
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

st.header("Research tool")

# creating dropdowns
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# prompt template 
template=load_prompt('template.json')


# using chain instead of template.invoke and model.invoke
# we are able to use below chain concept only because of prompt template,
# is we used f-string then we can't use chain concept.


if st.button('Generate'):
    chain = template | model
    result = chain.invoke(
        {
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        }
    )
    st.write(result.content)  