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

greenAPI = API.GreenAPI(
    "7103906718", "9af7993a489c4a279b9f20e1346265978085ea983f83420a82"
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
                rememberMessage = text.replace("jarvis","")
                speak("saya akan mengingat"+rememberMessage)
                remember = open("Remember.txt","a")
                remember.write(rememberMessage)
                remember.close()

            elif "kamu ingat" in text or "ingat apa" in text:
                remember = open("Remember.txt","r")
                speak("hal yang saya ingat adalah" + remember.read())

            elif "whatsapp" in text:
                # thread_b.start()
                
                pass

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
def incoming_message_received(body: dict) -> None:
    # from main import talk
    timestamp = body["timestamp"]

    senderName = body["senderData"]["senderName"] 
    senderNumber = body["senderData"]["sender"]
    text= ""
    groupName = ""
    if(body["messageData"]["typeMessage"] == "extendedTextMessage"):
        #pc
        groupName = groupName + " di " + body["senderData"]["chatName"]

        text = text + body["messageData"]["extendedTextMessageData"]["text"]
    elif(body["messageData"]["typeMessage"] == "textMessage"):
        # gc
        text = text + body["messageData"]["textMessageData"]["textMessage"]
        
    # print(grouptext)
    notify('pesan baru dari '+ senderName + ', '+ text + groupName)

    # print(f'new message from {senderName} number {senderNumber},  ')
    # print(f"New incoming message at {time} with data: {data}", end="\n\n")
    
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