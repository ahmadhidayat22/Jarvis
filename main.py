import speech_recognition as sr
import pyttsx3
import datetime
import os
from dotenv import load_dotenv , find_dotenv

import google.generativeai as genai


load_dotenv(find_dotenv())


API_KEY= os.getenv('BARD_API')

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')

listener = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('rate', rate-20)

# set voice speech. voices[0] => male, english ; voices[1]=> male ,indo ; voices[2]=> female, english;
 
engine.setProperty('voice', voices[1].id)



def talk(text):
   print(text)
   engine.say(text)
   engine.runAndWait()

def take_command():
         try:
            with sr.Microphone() as mic:
                print('listening...')
                listener.adjust_for_ambient_noise(mic, duration=0.2)
                audio = listener.listen(mic)
                text = listener.recognize_google(audio , language='id')
                text = text.lower()
                if 'jarvis' in text:
                  text = text.replace('jarvis', '')
                  print(f"Recognized : {text}")
                  return text


                else :
                    print('unknown command')
         except sr.UnknownValueError:
            pass
            
            # print('jarvis could not understand audio')
            # listener = sr.Recognizer()
           

def jarvis():
    
   print('running jarvis...')
   engine.say('halo')
   engine.say('apa yang bisa saya lakukan ?')
   engine.runAndWait()
   while True:

      command = take_command()
      print (command)
      

      if 'jam' in command:
         time = datetime.datetime.now().strftime('%I:%M %p')
         talk('Sekarang ' + time)

      elif 'stop' in command:
         talk('goodbye sir')
         return False
      else:
         response = model.generate_content(command)
         result = response.text
         talk(result)

       
      

jarvis()