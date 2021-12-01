def fetch_stats(selected_data, data):
    if selected_data != "Overall":

        data = data[data["user"] == selected_data]

    num_messages = data.shape[0]
    
    words = []
    for message in data["message"]:
        words.extend(message.split())

    return num_messages, len(words)
    