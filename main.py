import streamlit as st
from langchain import HuggingFaceHub
import os

st.title('LangChain - HuggingFace Demo App')
HUGGINGFACEHUB_API_TOKEN = st.sidebar.text_input('HuggingFace API Key')
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN


def generate_response(input_text):
    llm = HuggingFaceHub(repo_id='google/flan-t5-xxl', model_kwargs={"temperature": 0.5, "max_length": 64})
    st.info(llm(input_text))


with st.form('my_form'):
    text = st.text_area('Enter text: ')
    submitted = st.form_submit_button('Submit')
    if len(HUGGINGFACEHUB_API_TOKEN) <= 0:
        st.warning('API Key not found, Please enter API Key', icon='⚠️')
    if submitted and len(HUGGINGFACEHUB_API_TOKEN):
        generate_response(text)

