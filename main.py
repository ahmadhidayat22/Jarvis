import speech_recognition as sr
import pyttsx3
import os
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv , find_dotenv
import datetime
import asyncio
from whatsapp_api_client_python import API
import threading
import playsound
from gtts import gTTS

import time
from json import dumps
import time
from datetime import datetime
import requests

load_dotenv(find_dotenv())


idInstance = os.getenv('idInstance')
ApiTokenInstance = os.getenv('ApiTokenInstance')


greenAPI = API.GreenAPI(
    idInstance, ApiTokenInstance
)

engine2 = pyttsx3.init("sapi5")
rate = engine2.getProperty('rate')
voices = engine2.getProperty('voices')
volume = engine2.getProperty('volume')
engine2.setProperty('rate', rate+10)
engine2.setProperty('volume', volume+100)


# set voice speech. voices[0] => male, english ; voices[1]=> male ,indo ; voices[2]=> female, english;
engine2.setProperty('voice', voices[1].id)

song = AudioSegment.from_mp3("listening.mp3")

def notify(text):
  print(text)
  tts = gTTS(text, lang='id')
  format = 'machine.mp3'
  tts.save(format)
  playsound.playsound(format)
  os.remove(format)

def talk(text):
   print(text)

   engine2.say(text)
   engine2.runAndWait()

def take_command():
         listener = sr.Recognizer()
         
         with sr.Microphone() as mic:
               print('=> listening...')
               listener.adjust_for_ambient_noise(mic, duration=0.3)
               listener.pause_threshold = 1
               listener.energy_threshold = 600
               audio = listener.listen(mic)
             
         text = " "

         try:
            print('=> understanding....')
            
            text = listener.recognize_google(audio , language='id')
            text = text.lower()
            print(f"You : {text}")

           
         except sr.RequestError as er:
             print('=> Request error from google spech recognition '+er)

         except Exception as e:
                print("say that again")
                return "None"

         return text

def call(text):

   action_call = "jarvis"
   text = text.lower()
   if action_call in text:
      play(song)
      return True
   return False

def app():
    
    while True:
      # try:
        text = take_command()
        # text = "wake up"
        print(text)
        speak = ""

        if "wake up" in text:
          from greetMe import greetMe
          greetMe()
          
          while True:
            text = take_command()
            # text = "whatsapp"
            if  'jam berapa sekarang' in text or 'sekarang jam berapa' in text or 'jam' in text :
              time = datetime.datetime.now().strftime('%I:%M %p')
              talk("sekarang jam"+ time)

    
              
            elif "google" in text:
                from SearchNow import searchGoogle
                searchGoogle(text)
            elif "youtube" in text or "yt" in text or "musik" in text:
                from SearchNow import searchYoutube
                searchYoutube(text)
            # elif "wikipedia" in text:
            #     from SearchNow import searchWikipedia
            #     searchWikipedia(text)

            elif "suhu" in text or "cuaca" in text :
                from weather import main
                main(text)

            elif "ingat ini" in text:
                rememberMessage = text.replace("ingat ini","")
                # rememberMessage = text.replace("jarvis","")
                print(rememberMessage)
                talk("saya akan mengingat"+rememberMessage)
                remember = open("Remember.txt","a")
                remember.write(rememberMessage)
                remember.close()

            elif  "ingat apa" in text or "kamu ingat apa" in text :
                remember = open("Remember.txt","r")

                speak("hal yang saya ingat adalah" + remember.read())

            elif "whatsapp" in text:
                # thread_b.start()
                
                pass

                talk("hal yang saya ingat adalah" + remember.read())

            elif "lupakan" in text :
                talk("oke saya akan melupakan hal tersebut")
                os.remove("Remember.txt")

            elif "whatsapp" in text:
                thread_b = threading.Thread(target=webhook)
                thread_b.start()

                # pass


            elif "stop" in text:
                talk('oke bos, panggil saya jika anda membutuhkan')
                break

            elif "off" in text:
                talk('panggil saya lain kali sir')
                
                exit()

          

            elif "nanya" in text or "bertanya" in text or "tanya" in text :
              from gemini import main
              main(text)



            # time.sleep(1)
            
                
            # from case import state
            # speak = speak + state(text)

            # if speak == "False":
            #   talk('okay sir')
            #   exit()

            # talk(speak)
        
        
        # time.sleep(1)

      # except:
      #    talk('i dont understand')
      #    pass
        


from json import dumps
import time
import json
from queue import Queue


def webhook():
    # while True:
        # Lakukan tugas A
        try:
          greenAPI.webhooks.startReceivingNotifications(handler)

          time.sleep(1)
        except Exception as e:
            print(e)

            # pass
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
    # from main import talk
    timestamp = body["timestamp"]
    data = dumps(body, ensure_ascii=False, indent=4)

    senderName = body["senderData"]["senderName"] 
    senderNumber = body["senderData"]["sender"]
    text= ""
    groupName = ""
    typeMessage = body["messageData"]["typeMessage"] 
    blockGroup = ["BOT LAMIN" ,  "Loker TGR-SMD & OLL SHOP", "INFO LOKER KALTIM PERGUDANGAN/DISTRIBUTOR🔥🔥🔥"]
    if(typeMessage == "extendedTextMessage"):
        #pc

        text = text + body["messageData"]["extendedTextMessageData"]["text"]
    elif(typeMessage == "textMessage"):
        # gc
        text = text + body["messageData"]["textMessageData"]["textMessage"]
        groupName = groupName + " di " + body["senderData"]["chatName"]
        
    elif(typeMessage == "quotedMessage"):
        # gc
        if (body["messageData"]["textMessageData"]["quotedMessage"]["typeMessage"] == "textMessage"):

            text = text + body["messageData"]["textMessageData"]["quotedMessage"]["textMessage"]
            groupName = groupName + " di " + body["senderData"]["chatName"]
        
    # print(grouptext)
    if groupName in blockGroup :    
        # print(body)
        notify('pesan dari '+ senderName + ', '+ text + groupName)

    # print(f'new message from {senderName} number {senderNumber},  ')
    # print(f"New incoming message at {time} with data: {data}", end="\n\n")
# def delete_notif_message(id: int):
#     url = "https://api.greenapi.com/waInstance7103906718/deleteNotification/9af7993a489c4a279b9f20e1346265978085ea983f83420a82/43"
#     payload = {}
#     headers= {
#         "Content-Type":"application/json"
#     }

#     response = requests.request("DELETE", url, headers=headers, data = payload)

#     print(response.text.encode('utf8'))

def outgoing_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"New outgoing message at {time} with data: {data}", end="\n\n")


def outgoing_api_message_received(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print("New outgoing API message at" + time + " with data: "+ data)
    # notify("New outgoing API message at" + time + " with data: "+ data)


def outgoing_message_status(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    response = (
        f"Status of sent message has been updated at {time} with data: {data}"
    )
    print("Status of sent message has been updated at " + time + " with data: "+ data)
    # notify("Status of sent message has been updated at " + time + " with data: "+ data)


def state_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)
    print("Current instance state at  " + time + " with data: "+ data)
    # notify("Current instance state at  " + time + " with data: "+ data)


def device_info(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

 
    print("informasi perangkat sekarang  " + time + " with data: "+ data)
    # notify("informasi perangkat sekarang  " + time + " with data: "+ data)


def incoming_call(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)
    senderName = body["senderData"]["senderName"] 

    data = dumps(body, ensure_ascii=False, indent=4)

    # notify("Ada telepon masuk dari" + senderName)
    print(data)


def status_instance_changed(body: dict) -> None:
    timestamp = body["timestamp"]
    time = get_notification_time(timestamp)

    data = dumps(body, ensure_ascii=False, indent=4)

    print(f"status instansi sekarang {time} dengan data: {data}", end="\n\n")

# thread_a = threading.Thread(target=app)

# thread_b = threading.Thread(target=webhook)


# thread_a.start()

def read_json():

    while True:
        try:
            f = open('text.json')
            data = json.load(f)
            
            if data:
               

                data.pop(0)
                open("text.json", "w").write(
                    json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
                )
                time.sleep(1)

                # for i in range(len(data)):
                #     sender_name = data[0]['from']
                #     text= data[0]['text']
                #     phoneNumber= data[0]['number']
                #     groupName = data[0]['groupName']
                #     # print(f'{text} from {sender_name} in {groupName} ')
                #     # # q.pop(j)
                    

                #     msg = ''
                #     if(groupName == ''):
                #         msg='dari ' + sender_name + ', pesan: '+ text 
                #     else:
                #         msg= 'dari ' + sender_name + ' di ' + groupName +', pesan: '+ text
                #     notify(msg)
                    
                #     # q.append(data[i])
                
                #     # print(data[i]['from'])
                #     # print(f'{text} from {sender_name} [{phoneNumber}] in {groupName} ')
                #     # msg = ''
                #     # if(groupName == ''):
                #     #     msg='dari ' + sender_name + ', pesan: '+ text 
                #     # else:
                #     #     msg= 'dari ' + sender_name + ' di ' + groupName +', pesan: '+ text

                #     # notify(msg)

                f.close()
                
            time.sleep(1)
        except Exception as e:
            print(e)

threading.Thread(target=read_json).start()

if __name__ == '__main__':
    app()
