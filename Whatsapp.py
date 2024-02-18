import pywhatkit
import pyttsx3
import datetime
import speech_recognition
# import webbrowser
# from bs4 import BeautifulSoup
# from time import sleep
# import os 
# from datetime import timedelta
# from datetime import datetime

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)
# rate = engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# def takeCommand():
#     r = speech_recognition.Recognizer()
#     with speech_recognition.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold = 1
#         r.energy_threshold = 300
#         audio = r.listen(source,0,4)

#     try:
#         print("Understanding..")
#         query  = r.recognize_google(audio,language='en-in')
#         print(f"You Said: {query}\n")
#     except Exception as e:
#         print("Say that again")
#         return "None"
#     return query

# strTime = int(datetime.now().strftime("%H"))
# update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

from datetime import datetime
from json import dumps

from whatsapp_api_client_python import API
greenAPI = API.GreenAPI(
    "7103906718", "9af7993a489c4a279b9f20e1346265978085ea983f83420a82"
)


def main():
    greenAPI.webhooks.startReceivingNotifications(handler)
   


def handler(type_webhook: str, body: dict) -> None:
    if type_webhook == "incomingMessageReceived":
        incoming_message_received(body)
    elif type_webhook == "outgoingMessageReceived":
        outgoing_message_received(body)
    elif type_webhook == "outgoingAPIMessageReceived":
        outgoing_api_message_received(body)
    elif type_webhook == "outgoingMessageStatus":
        outgoing_message_status(body)
    elif type_webhook == "stateInstanceChanged":
        state_instance_changed(body)
    elif type_webhook == "deviceInfo":
        device_info(body)
    elif type_webhook == "incomingCall":
        incoming_call(body)
    elif type_webhook == "statusInstanceChanged":
        status_instance_changed(body)


def get_notification_time(timestamp: int) -> str:
    return str(datetime.fromtimestamp(timestamp))


def incoming_message_received(body: dict) -> None:
    from main import talk
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    senderName = body["senderData"]["chatName"] 
    senderNumber = body["senderData"]["sender"]
    # text = body["messageData"]["textMessageData"]["textMessage"]
    text= ""
    if(body["messageData"]["typeMessage"] == "extendedTextMessage"):
        text = text + body["messageData"]["extendedTextMessageData"]["text"]
    elif(body["messageData"]["typeMessage"] == "textMessage"):
        text = text + body["messageData"]["textMessageData"]["textMessage"]
        
    
    print(text)
    # talk('pesan baru dari '+ senderName + ', '+ text)

    # print(f'new message from {senderName} number {senderNumber}, say: {text} ')
    # print(f"New incoming message at {time} with data: {data}", end="\n\n")
    return



def outgoing_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New outgoing message at {time} with data: {data}", end="\n\n")


def outgoing_api_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New outgoing API message at {time} with data: {data}", end="\n\n")


def outgoing_message_status(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    response = (
        f"Status of sent message has been updated at {time} with data: {data}"
    )
    print(response, end="\n\n")


def state_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"Current instance state at {time} with data: {data}", end="\n\n")


def device_info(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    response = (
        f"Current device information at {time} with data: {data}"
    )
    print(response, end="\n\n")


def incoming_call(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New incoming call at {time} with data: {data}", end="\n\n")


def status_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"Current instance status at {time} with data: {data}", end="\n\n")

if __name__ == '__main__':
    main()