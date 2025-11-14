import streamlit as st
import pandas as pd

def run():

    file_cleaned_path = "./data/cleaned/wine_data_cleaned.csv"
    df = pd.read_csv(file_cleaned_path)


    st.write("""
    # App web
    """)

    st.write(df.head())
    st.write(df.describe())


if __name__ == "__main__":
    run()