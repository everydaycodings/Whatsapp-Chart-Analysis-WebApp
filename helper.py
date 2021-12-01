def fetch_stats(selected_data, data):
    if selected_data == "Overall":
        return data.shape[0]
    
    else:
        return data[data["user"] == selected_data].shape[0]