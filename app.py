import streamlit as st
import pandas as pd

# Title of the application
st.title("Excel File Upload and Duplicate Remover")

# File uploader widget
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Read the Excel file
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    
    # Display the original data
    st.write("### Original Data")
    st.write(df)
    
    # Checkbox to remove duplicates
    if st.checkbox("Remove duplicates"):
        # Remove duplicates
        df_cleaned = df.drop_duplicates()
        
        # Display the cleaned data
        st.write("### Data after removing duplicates")
        st.write(df_cleaned)
        
        # Option to download the cleaned data
        st.write("### Download Cleaned Data")
        st.download_button(
            label="Download cleaned data as Excel",
            data=df_cleaned.to_csv(index=False).encode('utf-8'),
            file_name='cleaned_data.csv',
            mime='text/csv',
        )
else:
    st.write("Please upload an Excel file to get started.")