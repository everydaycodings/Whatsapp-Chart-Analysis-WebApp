from urlextract import URLExtract
from wordcloud import WordCloud

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


def created_world_cloud(selected_data, data):
    if selected_data != "Overall":
        data = data[data["user"] == selected_data]
    
    wc = WordCloud(width=600, height=300, min_font_size=10, background_color="white")
    df_wc = wc.generate(data["message"].str.cat(sep=" "))

    return df_wc