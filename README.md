# gen-ai

# 🛍️ E-Commerce Product Assistant using Groq, LangChain, and Streamlit

This project is a smart conversational assistant that extracts **structured product information** from user queries using LLMs. It leverages:

- 🔗 [LangChain](https://www.langchain.com/) for LLM orchestration  
- 🧠 [Groq](https://console.groq.com/) for blazing-fast access to open-source LLMs (like LLaMA 3)  
- ✅ [Pydantic](https://docs.pydantic.dev/) for output validation  
- 💻 [Streamlit](https://streamlit.io/) for a lightweight UI

---

## ✨ Demo

👉 [Watch the Demo Video](#)  
📂 [View the Code (app.py)](https://github.com/reetibhagat/gen-ai/blob/main/Langchain%20Basics/app.py)

---

## 💡 Features

- Ask about any e-commerce product (e.g., headphones, phones, laptops)
- Extracts:
  - `product_name`
  - `product_details`
  - `price_usd` (as int or float)
- Displays results in a clean Streamlit interface
- Powered by Groq-hosted **LLaMA 3** model via LangChain integration

---

## 📦 Requirements

```bash
pip install -r requirements.txt
