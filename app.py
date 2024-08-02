import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import BambooLLM
from config import settings

KEY = settings.pandas_api_key
llm = BambooLLM(api_key=KEY)

st.title("Data analysis with PandasAI")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, encoding="latin-1")
    st.write(data.head(3))

    df = SmartDataframe(data, config={"llm": llm})
    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(df.chat(prompt))
