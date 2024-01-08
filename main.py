from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import pandasAI
from pandasai.llm import OpenAI
import matplotlib
matplotlib.use('TkAgg')


load_dotenv()

API_KEY=os.environ['OPENAI_API_KEY']
#print(API_KEY)

llm=openAI(api_token=API_KEY)
pandas_ai=pandasAI(llm)
st.title("Prompt-driven analysis with pandasAI")

uploaded_file=st.file_uploader("upload a csv/excel file for Analysis",type=['csv','excel'])

if uploaded_file is not None:

    df=pd.read_csv(uploaded_file)
    st.write(df.head(3))

    prompt=st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
           with st.spinner("Generating response..."):
           #st.write("PAndas AI is generating") 
            st.write(pandas_ai.run(df,prompt=prompt))
        
        else:
            st.warning("Waring enter the prompt")

