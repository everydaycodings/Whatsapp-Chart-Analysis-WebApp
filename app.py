import streamlit as st
import preprocessor

st.sidebar.title("Hello World")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    data = preprocessor.preprocess(data)
    st.dataframe(data)

    user_list = data["user"].unique().tolist()
    #st.sidebar.selectbox("Show Analysis with Respect to {}".format(user_list))

    option = st.sidebar.selectbox('Which user would you like to see Analysis',
      (user_list))

    st.write('Show Analysis with Respect to', option)