from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter

extract = URLExtract()

def fetch_stats(selected_data, data):
    if selected_data != "Overall":

        data = data[data["user"] == selected_data]

    num_messages = data.shape[0]
    num_media_messages = data[data['message'] == '<Media omitted>\n'].shape[0]

    link = []
    for message in data["message"]:
        link.extend(extract.find_urls(message))
    
    words = []
    for message in data["message"]:
        words.extend(message.split())

    return num_messages, len(words), num_media_messages, len(link)



def fetch_most_active_user(data):

    x = data["user"].value_counts().head()

    result = round((data["user"].value_counts()/data.shape[0])*100, 1).reset_index().rename({"index":"user", "user":"perentage"})

    return x, result


def created_word_cloud(selected_data, data):
    if selected_data != "Overall":
        data = data[data["user"] == selected_data]
    
    wc = WordCloud(width=600, height=300, min_font_size=10, background_color="white")
    df_wc = wc.generate(data["message"].str.cat(sep=" "))

    return df_wc


def most_common_words(selected_user,data):

    f = open('stop_hinglish.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        data = data[data['user'] == selected_user]

    temp = data[data['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_data = pd.DataFrame(Counter(words).most_common(20))
    return most_common_data

def emoji_helper(selected_user,data):
    if selected_user != 'Overall':
        data = data[data['user'] == selected_user]