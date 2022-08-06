import time
import applescript
from imessage_reader import fetch_data
from datetime import datetime


def send_message(nr, message):
    script = '''
    on run {input, parameters}
    tell application "Messages"
        set targetBuddy to (item 1 of input)
        set targetService to id of 1st account whose service type = SMS
        set textMessage to (item 2 of input)
        set theBuddy to participant targetBuddy of account id targetService
        send textMessage to theBuddy
    end tell
    return input
    end run
    '''
    applescript.AppleScript(script).run([nr, message], 1)


def sort_messages(messages: list):
    messages.sort(key=lambda x: x[2])


def access_messages(nr):
    fd = fetch_data.FetchData()
    data = fd.get_messages()
    filtered_messsages = []

    for m in data:
        if m[0] == nr:
            filtered_messsages.append(m)

    return filtered_messsages


def print_messages(messages):
    text = [(x[1], x[5]) for x in messages]

    for m in text:
        if m[1] == 0:
            print(f'William: {m[0]}\n')
        else:
            print(f'Emil: {m[0]}\n')


message_not_sent = True
while message_not_sent:
    messages = access_messages('+4673749404643')
    sort_messages(messages)

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        if current_time[0:10] == messages[-1][2][0:10]:
            if current_time[-5:-3] == messages[-1][2][-5:-3]:
                if "C tur" in messages[-1][1] or "B tur" in messages[-1][1]:
                    print("sending!! but gotta wait like 3 seconds so it's not sus")
                    time.sleep(10)
                    send_message('+4673749404643', "Jag kan! / Emil Eberhard")
                    message_not_sent = False
    except IndexError:
        time.sleep(1)
