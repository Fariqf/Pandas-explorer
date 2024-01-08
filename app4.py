from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
import matplotlib
from pandasai.llm import OpenAI

matplotlib.use('TkAgg')

load_dotenv()

API_KEY=os.environ['OPENAI_API_KEY']

st.title("Prompt-driven analysis with pandasAI")
uploaded_file=st.file_uploader("upload a csv/excel file for Analysis",type=['csv','excel'])

llm = OpenAI(api_token='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')
if uploaded_file is not None:

    df=pd.read_csv(uploaded_file)
    st.write(df.head(3))
    df = SmartDataframe(df, config={"llm": llm})
    prompt=st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
           with st.spinner("Generating response..."):
           #st.write("PAndas AI is generating") 
               st.write(df.chat(prompt))
        
        else:
            st.warning("Waring enter the prompt")

st.caption("Made with ❤️ by @fariq")