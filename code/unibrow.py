'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a csv, excel, or json file", type = ["csv", "xlsx", "json"])
if file:
    extension = pl.get_file_extension(file.name)
    df = pl.load_file(file, extension)
    col_names = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to view: ", col_names, default = col_names[0])
    if st.toggle("Filter data"):
        text_cols = pl.get_columns_of_type(df, "object")
        filter_col = st.selectbox("Select column to filter on: ", text_cols)
        if filter_col:
            values = pl.get_unique_values(df, filter_col)
            selected_val = st.selectbox("Select value to filter for: ", values)
            modified_df = df[df[filter_col] == selected_val][selected_cols]
    else:
        modified_df = df[selected_cols]
    
    st.dataframe(modified_df)
    st.dataframe(modified_df.describe())

        

