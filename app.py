import streamlit as st
import preprocessor, helper

st.sidebar.title("Hello World")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    data = preprocessor.preprocess(data)
    st.dataframe(data)

    user_list = data["user"].unique().tolist()
    user_list.sort()
    user_list.remove("group_notification")
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox('Which user would you like to see Analysis',(user_list))

    if st.sidebar.button("Show Analysis"):
        num_messages = helper.fetch_stats(selected_user, data)

        col1, clo2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)