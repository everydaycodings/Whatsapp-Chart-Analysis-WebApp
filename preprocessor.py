import re
import pandas as pd

def preprocess(data):

    dissision_pattern = "\d{1,2}:\d{2}\s[AaPp][Mm]"
    dission = len(re.findall(dissision_pattern, data))

    if dission >= 3:
        pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[AaPp][Mm]\s-\s"
        pattern1 = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[AaPp][Mm]"
        messages = re.split(pattern, data)[1:]
        dates = re.findall(pattern1, data)

        data = pd.DataFrame({"user_message": messages, "date": dates})
        data["date"] = pd.to_datetime(data["date"], format="%d/%m/%Y, %I:%M %p")
        data = data[["date", "user_message"]]
    
    else:
        pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

        messages = re.split(pattern, data)[1:]
        dates = re.findall(pattern, data)

        data = pd.DataFrame({'user_message': messages, 'date': dates})
        # convert message_date type
        data['date'] = pd.to_datetime(data['date'], format='%d/%m/%Y, %H:%M - ')

        data = data[["date", "user_message"]]

    users = []
    messages = []
    for message in data['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    data['user'] = users
    data['message'] = messages
    data.drop(columns=['user_message'], inplace=True)


    data['only_date'] = data['date'].dt.date
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month_name()
    data['day'] = data['date'].dt.day
    data['day_name'] = data['date'].dt.day_name()
    data['hour'] = data['date'].dt.hour
    data = data.drop(columns="date")
    data = data[["only_date", "year", "month", "day", "day_name", "hour", "user", "message"]]
    data = data.rename(columns = {'only_date':'date'})

    return data