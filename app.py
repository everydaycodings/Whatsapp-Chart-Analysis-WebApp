import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt

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
        num_messages, words, num_media_messages, link = helper.fetch_stats(selected_user, data)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.subheader("Total Messages Contributed by {}".format(selected_user))
            st.title(num_messages)
        
        with col2:
            st.subheader("Total Words of Messages by {}".format(selected_user))
            st.title(words)
        
        with col3:
            st.subheader("Total Media Shared by {}".format(selected_user))
            st.title(num_media_messages)
        
        with col4:
            st.subheader("Total Link Shared by {}".format(selected_user))
            st.title(link)
        
        if selected_user == "Overall":
            
            st.subheader("Top 5 Most Active Users and Percentage contribution made by user")

            x,percent_data = helper.fetch_most_active_user(data)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color="red")
                plt.xticks(rotation=80)
                st.pyplot(fig)
            
            with col2:
                st.dataframe(percent_data)
