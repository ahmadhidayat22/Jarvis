import google.generativeai as genai
import speech_recognition as sr
from dotenv import load_dotenv , find_dotenv
import os
import pyttsx3
from IPython.display import display
from IPython.display import Markdown
import pathlib
import textwrap
load_dotenv(find_dotenv())


API_KEY= os.getenv('BARD_API')

genai.configure(api_key=API_KEY)

# model = genai.GenerativeModel('gemini-pro')

generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 200,
  "max_output_tokens": 2048,
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

chat = model.start_chat(history=[])

# chat = model.start_chat(history=[
#   {
#     "role": "user",
#     "parts": ["kamu adalah Leo, asisten ai yang ramah dan sangat menyenangkan."]
#   },
#   {
#     "role": "model",
#     "parts": ["Halo! Saya Leo, asisten AI yang ramah dan menyenangkan. Saya di sini untuk membantu Anda dengan apa pun yang Anda perlukan. Saya dapat membantu Anda dengan tugas, menjawab pertanyaan, atau sekadar mengobrol. Saya selalu ingin tahu dan belajar, jadi jangan ragu untuk mengajukan pertanyaan apa pun kepada saya. Saya akan melakukan yang terbaik untuk membantu!"]
#   },
# ])

chat = model.start_chat(history=[])


engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('rate', rate+30)
engine.setProperty('volume', 150)

# set voice speech. voices[0] => male, english ; voices[1]=> male ,indo ; voices[2]=> female, english;
engine.setProperty('voice', voices[1].id)



def talk(text):
   print(text)
   engine.say(text)
   engine.runAndWait()

def take_command():
         listener = sr.Recognizer()
         
         with sr.Microphone() as mic:
               print('=> listening...')
               listener.adjust_for_ambient_noise(mic, duration=0.2)
               listener.pause_threshold = 1
               listener.energy_threshold = 100
               audio = listener.listen(mic )
             
         text = " "

         try:
            print('=> understanding....')
            
            text = listener.recognize_google(audio , language='id')
            text = text.lower()
            print(f"You : {text}")
           
         except sr.RequestError as er:
            print('=> Request error from google spech recognition '+er)
            return "None"

         except Exception as e:
                  print("say that again")
                  return "None"
            # print('jarvis could not understand audio')
            # listener = sr.Recognizer()
         return text


def main(text):
    while True:
      talk('hai tuan apakah ingin bertanya ? ')

      text = take_command()
      # text = "apa itu python"
      
      if not "None" in text:

        if 'ya' in text or "iya" in text :
          talk('ingin bertanya apa')
          text = take_command()
          
          if not "None" in text:
            text = text.replace("ya", "")
            text = text.replace("iya", "")
            
            response = chat.send_message(text, stream=True)
            for chunk in response:
                result = chunk.text
                # print(result)
                talk(result)
        elif 'tidak' in text or 'nggak' in text or 'sudah' in text  :
          talk('oke terimakasih telah bertanya ')
           
          break
    return




# ide fitur
# hasil response ai bisa ditaruh kedalam array kemudian, di tampilkan hanya sebagaian kecil saja, kalau ingin dengar semua kasih sebuah perintah