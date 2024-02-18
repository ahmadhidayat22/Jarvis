# import threading
# import time
# from whatsapp_api_client_python import API
# greenAPI = API.GreenAPI(
#     "7103906718", "9af7993a489c4a279b9f20e1346265978085ea983f83420a82"
# )

# def func_a():
#     while True:
#         # Lakukan tugas A
#         greenAPI.webhooks.startReceivingNotifications(handler)

#         time.sleep(1)
# def handler(type_webhook: str, body: dict) -> None:
#     if type_webhook == "incomingMessageReceived":
#         incoming_message_received(body)

# def incoming_message_received(body: dict) -> None:
#     # from main import talk
#     timestamp = body["timestamp"]

#     senderName = body["senderData"]["chatName"] 
#     senderNumber = body["senderData"]["sender"]
#     text = body["messageData"]["textMessageData"]["textMessage"]
    
#     print(text)
#     # talk('pesan baru dari '+ senderName + ', '+ text)

#     # print(f'new message from {senderName} number {senderNumber},  ')
#     # print(f"New incoming message at {time} with data: {data}", end="\n\n")
    



# def func_b():
#     while True:
#         # Lakukan tugas B berdasarkan state

#         a = input("masukkan kalimat : ")
#         print(a)

#         time.sleep(1)

# thread_a = threading.Thread(target=func_a)
# thread_b = threading.Thread(target=func_b)

# thread_a.start()
# thread_b.start()
import playsound
import os
from gtts import gTTS

text= "hallo ini test satu dua tiga dengan bahasa indonesia"

tts = gTTS(text, lang='id')
format = 'test.mp3'
tts.save(format)
playsound.playsound(format)
os.remove(format)