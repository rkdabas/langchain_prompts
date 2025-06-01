from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# This is will not work, because langchain doesn't work like this in ChatPromptTemplate
# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert."),
#     HumanMessage(content="Explain in simple terms, what is {topic}")
# ])

# This is the correct way to use ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ('system',"you are a helpful {domain} expert."),
    ('human',"Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({
    'domain':'football',
    'topic':'offside rule in football?'
})

print(prompt)