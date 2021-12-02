from urlextract import URLExtract

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
    return x