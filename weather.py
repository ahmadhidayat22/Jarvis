import pywhatkit
import os
import requests
import pyttsx3
import speech_recognition as sr


from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())


WEATHER_KEY = os.getenv('WEATHER_KEY')


engine = pyttsx3.init("sapi5")
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume')
engine.setProperty('rate', rate+10)
engine.setProperty('volume', volume+100)

def talk(text):
   print(text)
   engine.say(text)
   engine.runAndWait()

def take_command():
         listener = sr.Recognizer()
         
         with sr.Microphone() as mic:
               print('=> listening...')
               listener.adjust_for_ambient_noise(mic, duration=0.3)
               listener.pause_threshold = 1
               listener.energy_threshold = 100
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




def main(text):
    
    try:
        key = WEATHER_KEY
        url_weather = "https://api.openweathermap.org/data/2.5/weather?"
        ind = text.split().index("di")
        
        location = text.split()[ind + 1:]
        location = "".join(location)
        url = url_weather +"q="+ location+ "&appid="+key
        js = requests.get(url).json()
        if js["cod"] != "404":
            weather = js["main"]
            temperature = weather["temp"]
            temperature = round(temperature - 273.15)
            # humidity = weather["humidity"]
            desc= js["weather"][0]["description"]
            weatherRes = "suhu sekarang sekitar "+ str(temperature) +" derajat celcius" + " dan " + str(desc)
            talk(weatherRes)

        else:
            talk("kota tidak ditemukan")
    except Exception as e:
        talk("ada sedikit kesalahan, coba lagi")
         
        return
    
    