import speech_recognition as sr
import pyttsx3
import datetime
import os
from dotenv import load_dotenv , find_dotenv

import google.generativeai as genai
 
# import required module
from playsound import playsound

# import required modules
from pydub import AudioSegment
from pydub.playback import play

load_dotenv(find_dotenv())


API_KEY= os.getenv('BARD_API')

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

listener = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('rate', rate+10)

# set voice speech. voices[0] => male, english ; voices[1]=> male ,indo ; voices[2]=> female, english;
engine.setProperty('voice', voices[1].id)

song = AudioSegment.from_mp3("listening.mp3")



def talk(text):
   print(text)
   engine.say(text)
   engine.runAndWait()

def take_command():
         try:
            with sr.Microphone() as mic:
               print('listening...')
               play(song)
               listener.adjust_for_ambient_noise(mic, duration=0.2)
               audio = listener.listen(mic)
               text = listener.recognize_google(audio , language='id')
               text = text.lower()
               print(f"You : {text}")
               if 'jarvis' in text:
                  text = text.replace('jarvis', '')
                  print(f"Jarvis : {text}")
                  return text


               else :
                  print('unknown command')
                  return 'pass'
                  # take_command()

         except sr.UnknownValueError :
            return 'pass'
            pass
            
            # print('jarvis could not understand audio')
            # listener = sr.Recognizer()
           

def jarvis():
   loop = True
   print('running jarvis...')
   engine.say('halo')
   engine.say('apa yang bisa saya lakukan ?')
   engine.runAndWait()
   print('give a command after "beep"..')
   while loop:


      command = take_command()
      # print (command)
      
      if command != 'None':
         if 'jam' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Sekarang ' + time)

         elif 'stop' in command:
            talk('goodbye ser')
            loop = False 
         
         elif 'pass' in command:
            continue
         else:
            response = chat.send_message(command , stream=True)
            for chunk in response:
               result = chunk.text
               print(chunk.text)
               talk(result)
      else:
         print('ini none')


   if(loop == False):
       return
 

jarvis()