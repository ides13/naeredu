# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import openai
import pandas as pd
import streamlit as st


# Insert our openAI API key
# https://platform.openai.com/account/api-keys
#from getpass import getpass
#openai.api_key = getpass()
openai.api_key = "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"

st.title("📒 Notebook AI 🤖 ")


file_load = st.file_uploader("Upload Embeddings file")
if file_load:
    data = pd.read_csv(file_load)
# Display the DataFrame
    data

user_secret = st.text_input(
        label=":blue[OpenAI API key]",
        placeholder="Paste your openAI API key, sk-",
        type="password",
    )
if user_secret:
    openai.api_key = user_secret

    # Get the search term from the user through a text input widget
    search_term = st.text_input(
        label=":blue[Search your Query]",
        placeholder="Please, search my notebook with...",
    )

    # Get the search button trigger from the user
    search_button = st.button(label="Run", type="primary")
    

    
    
    