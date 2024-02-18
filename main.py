import speech_recognition as sr
import pyttsx3
import os
from pydub import AudioSegment
from pydub.playback import play
from dotenv import load_dotenv , find_dotenv
import google.generativeai as genai


load_dotenv(find_dotenv())


API_KEY= os.getenv('BARD_API')

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')


chat = model.start_chat(history=[])
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

chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["kamu adalah Leo, asisten ai yang ramah dan sangat menyenangkan."]
  },
  {
    "role": "model",
    "parts": ["Halo! Saya Leo, asisten AI yang ramah dan menyenangkan. Saya di sini untuk membantu Anda dengan apa pun yang Anda perlukan. Saya dapat membantu Anda dengan tugas, menjawab pertanyaan, atau sekadar mengobrol. Saya selalu ingin tahu dan belajar, jadi jangan ragu untuk mengajukan pertanyaan apa pun kepada saya. Saya akan melakukan yang terbaik untuk membantu!"]
  },
])


engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('rate', rate+10)
# engine.setProperty('volume', volume+20)

# set voice speech. voices[0] => male, english ; voices[1]=> male ,indo ; voices[2]=> female, english;
engine.setProperty('voice', voices[1].id)

song = AudioSegment.from_mp3("listening.mp3")



def talk(text):
   print(text)
   engine.say(text)
   engine.runAndWait()

def take_command():
         listener = sr.Recognizer()
         
         with sr.Microphone() as mic:
               print('=> listening...')
               listener.adjust_for_ambient_noise(mic, duration=0.2)
               # listener.pause_threshold = 1
               # listener.energy_threshold = 300
               audio = listener.listen(mic )
             
         text = " "

         try:
            print('=> understanding....')
            
            text = listener.recognize_google(audio , language='id')
            text = text.lower()
            # print(f"You : {text}")
            # if 'jarvis' in text:
            #    text = text.replace('jarvis', '')
            #    print(f"Jarvis : {text}")
            #    return text


            # else :
            #    print('unknown command')
            #    return 'pass'
            #    #  
         
         # except sr.UnknownValueError :
         #    print('=> leo could not understand the audio')
           
         except sr.RequestError as er:
             print('=> Request error from google spech recognition '+er)

         except Exception as e:
                  print("say that again")
                  return "None"
            # print('jarvis could not understand audio')
            # listener = sr.Recognizer()
         return text

def call(text):

   action_call = "leo"
   text = text.lower()
   if action_call in text:
      play(song)
      return True
   return False



if __name__ == "__main__":
   while True:
      try:
         # text = take_command()
         text = "leo"
         speak = ""

         print(f"You : {text}")
         if call(text):
            from case import state
            speak = speak + state(text)

            if speak == "False":
               talk('oke ser, panggil aku kapan pun yang kamu mau')
               break

            talk(speak)

      except:
         talk('saya tidak paham')
         pass
        

# def jarvis():

#    loop = True
#    print('running jarvis...')
#    engine.say('halo')
#    engine.say('apa yang bisa saya lakukan ?')
#    engine.runAndWait()
#    print('give a command after "beep"..')
#    while loop:

#       command = take_command()
#       # print (command)
      
#       if command != 'None':
#          if 'jam' in command:
#             time = datetime.datetime.now().strftime('%I:%M %p')
#             talk('Sekarang ' + time)

#          elif 'stop' in command:
#             talk('goodbye ser')
#             loop = False 
         
#          elif 'pass' in command:
#             continue
#          else:
#             response = chat.send_message(command , stream=True)
#             for chunk in response:
#                result = chunk.text
#                # print(result)
#                talk(result)
#       else:
#          print('ini none')


#    if(loop == False):
#        return
 


# if _main_ == "_main_":

   # jarvis()