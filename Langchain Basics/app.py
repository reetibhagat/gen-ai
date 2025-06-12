print("✅ app.py started running")

import os
from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
from pydantic import BaseModel, Field
from typing import Union
from langchain_groq import ChatGroq
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain


# Set API key (or use environment variable)
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
print("✅ app.py started running")
print("🔑 GROQ_API_KEY loaded:", os.getenv("GROQ_API_KEY"))  # Debug line


# Define schema
class ProductInfo(BaseModel):
    product_name: str
    product_details: str
    price_usd: Union[int, float]

parser = PydanticOutputParser(pydantic_object=ProductInfo)

# Prompt template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intelligent e-commerce assistant."),
    HumanMessagePromptTemplate.from_template("""
Given a user question about a product, extract:
- product_name
- product_details
- price_usd

Respond in the following JSON format:
{format_instructions}

Question: {user_question}
""")
])
prompt = chat_prompt.partial(format_instructions=parser.get_format_instructions())

# LLM
llm = ChatGroq(model="llama3-8b-8192", temperature=0)

# Chain
chain = LLMChain(llm=llm, prompt=prompt, output_parser=parser)

# Streamlit UI
st.title("🛍️ E-Commerce Product Assistant (Groq LLM)")
user_input = st.text_input("Ask a product-related question:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            result = chain.run(user_question=user_input)
            st.success("Here's the extracted product info:")
            st.json(result.dict())
        except Exception as e:
            st.error(f"Error: {e}")
print("✅ app.py started running")
print("🔑 GROQ_API_KEY loaded:", os.getenv("GROQ_API_KEY"))  # Debug line

...a
