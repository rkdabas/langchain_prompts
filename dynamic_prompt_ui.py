# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
# model=ChatOpenAI()
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

st.header("Research tool")

# creating dropdowns
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# prompt template 
template=PromptTemplate(
    template="""
Please summarize the reasearch paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical details:
    - Include relevant mathematical equations and notations if present in the paper.
    - Explain the mathematical concepts in a way that is easy to understand and using intuitive code snippets where applicable.

2. Analogies:
    - Use reletable analogies to simplify complex concepts.
If certain information in not available in the paper, response with "Insufficient information 
available" instead of quession.
Ensure the summary is clear, accurate, and alligned with the provided style and length.
""",
input_variables=["paper_input", "style_input", "length_input"]
)

# fill the placeholders
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})


if st.button('Generate'):
    result=model.invoke(prompt)
    st.write(result.content)  