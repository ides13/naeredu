# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import openai
import pandas as pd
import streamlit as st
from openai.embeddings_utils import cosine_similarity, get_embedding


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
    
