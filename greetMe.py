import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 250)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    day = ''
    if hour>=0 and hour<=12:
        day = day + 'pagi'
        speak("selamat pagi, Tuan")
    elif hour >12 and hour<=18:
        day = day + 'siang'

        speak("selamat siang, Tuan")

    else:
        day = day + 'malam'
        speak("selamat malam, Tuan")
    
    speak("sekarang jam "+ str(hour) + day)
    speak("ada yang bisa saya bantu ? ")