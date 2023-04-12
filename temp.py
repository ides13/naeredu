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
openai.api_key = ""

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
    
def search_notebook(df, search_term, n=3, pprint=True):
    """
    Search for the most similar notes in the dataframe `df` to the `search_term`.

    Args:
        df (pandas.DataFrame): DataFrame containing the notes to be searched through.
        search_term (str): The term to search for.
        n (int, optional): The number of results to return. Defaults to 3.
        pprint (bool, optional): Whether to print the results. Defaults to True.

    Returns:
        pandas.DataFrame: DataFrame containing the most similar notes to the `search_term`, sorted by similarity.
    """
    # Convert the embeddings in the 'embedding' column from strings to numpy arrays.
    df["embedding"] = df["embedding"].apply(eval).apply(np.array)

    # Get the embedding for the `search_term` using the "text-embedding-ada-002" engine.
    search_embeddings = get_embedding(search_term, engine="text-embedding-ada-002")

    # Calculate the cosine similarity between each note's embedding and the `search_term`'s embedding.
    df["similarity"] = df["embedding"].apply(
        lambda x: cosine_similarity(x, search_embeddings)
    )

    # Sort the notes by similarity in descending order and select the top `n` notes.
    results = df.sort_values("similarity", ascending=False).head(n)
    return results

    # If the user has entered a search term
if search_term:
    # And if they have clicked the search button
    if search_button:
        # Run the search function and get the results
        answer = search_notebook(data, search_term, 3, True)
        # Iterate through the results and display the similarity and notes
        for index, row in answer.iterrows():
            st.write(row["similarity"], row["Notes"])
else:
    st.info("Please Upload the embeddings file.")
    
    
    