from dotenv import load_dotenv , find_dotenv
from googletrans import Translator
#  pip install googletrans

import webbrowser
import requests
import datetime
import os
import pywhatkit
import random 
import pyttsx3


load_dotenv(find_dotenv())


WEATHER_KEY = os.getenv('WEATHER_KEY')

# def talk(text):
#    print(text)
#    engine.say(text)
#    engine.runAndWait()


def greeting(text):
   greet = ["hai" , "halo" , "hey", "leo"]
   response = ["whassup" , "halo" , "hey", "siap" , "ada apa", "bagaimana kabarmu"]
   for word in text.split():
      if word.lower() in greet:
          return random.choice(response) + " bos"
      
   return ""


def weather(text, apikey):
    speak= ""
    key = apikey
    url_weather = "https://api.openweathermap.org/data/2.5/weather?"
    ind = text.split().index("in")
    location = text.split()[ind + 1:]
    location = "".join(location)
    url = url_weather +"q="+ location+ "&appid="+key
    js = requests.get(url).json()
    print(url)
    if js["cod"] != "404":
        weather = js["main"]
        temperature = weather["temp"]
        temperature = round(temperature - 273.15)
        # humidity = weather["humidity"]
        desc= js["weather"][0]["description"]
        weatherRes = "suhu sekarang sekitar "+ str(temperature) +" derajat celcius" + " dan " + str(desc)
        speak = speak + weatherRes

    else:
        speak = speak + "kota tidak ditemukan"
    
    return speak


# def translategl(query):
#     translator = Translator()
#     translator.translate(query, src="auto")


def state(text):
    speak = ""
    speak = speak +  greeting(text)
    if 'jam' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak = "sekarang jam "+time

    elif 'cuaca sekarang in' in text :
       speak = speak + weather(text, WEATHER_KEY)
    elif 'youtube' in text :
        ind = text.lower().split().index('youtube')
        search = text.split()[ind +1:]
        search = " ".join(search)
        pywhatkit.playonyt(search)
        speak = speak + "mencari " + search +" di youtube"
    
    elif "buka" in text :
        pass

    

    elif 'stop' in text:
        return "False"

    return speak
    
    