def fetch_stats(selected_data, data):
    if selected_data == "Overall":

        words = []
        for message in data["message"]:
            words.extend(message.split())

        num_messages = data.shape[0]

        return num_messages, len(words)
    
    else:
        selected_data = data[data["user"] == selected_data]

        num_messages = selected_data.shape[0]
        
        words = []
        for message in selected_data["message"]:
            words.extend(message.split())
        
        return num_messages, len(words)