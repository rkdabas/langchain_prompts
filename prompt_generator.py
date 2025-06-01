from langchain_core.prompts import PromptTemplate

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
input_variables=["paper_input", "style_input", "length_input"],
validate_template=True
)

template.save('template.json')