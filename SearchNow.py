import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import time


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

# query = "who is donuld trump leo"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        while True:
            speak("oke, anda ingin mencari apa ?")
            time.sleep(1)
            query = takeCommand().lower()
            import wikipedia as googleScrap


            if query != "" or query != "None" :
                query = query.replace("leo","")
                query = query.replace("buka","")
                query = query.replace("google","")
                query = query.replace("cari","")
                query = query.replace("ke","")
                speak("ini yang aku temukan di google")

                try:
                    pywhatkit.search(query)

                    result = googleScrap.summary(query,5,auto_suggest=True)
                    speak(result)

                except:
                    speak("tidak ada yang dihasilkan sekarang")
                return False
            else: 
                continue

def searchYoutube(query):
    if "youtube" in query or "yt" in query or "music" in query:
        while True:
            speak("oke bos, ingin memutar youtube apa ?") 
           
            query = takeCommand().lower()
            print(query)

            # query = "wiz khalifa"
            if query != "" or query != "None" :
                speak("ini yang aku temukan") 
                query = query.replace("cari","")
                query = query.replace("youtube","")
                query = query.replace("leo","")
                web  = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(web)
                pywhatkit.playonyt(query)
                speak("Done, Sir")
                return False
            else: 
                continue
            
        

def searchWikipedia(query):
    if "wikipedia" in query:
        while True:
            
            speak("oke, anda ingin mencari apa ?") 
            query = takeCommand().lower()
            if query != "" or query != "None" :

                speak("mencari ke wikipedia")
                query = query.replace("wikipedia","")
                query = query.replace("cari","")
                query = query.replace("leo","")
                try:
                    results = wikipedia.summary(query,sentences=3,auto_suggest=True)
                    speak("berdasakan wikipedia.")
                    # print("According to wikipedia..")
                    # print(results)
                    speak(results)
                except Exception as e:
                    speak("berdasakan wikipedia.")

                    continue
                return False
            else: 
                continue
            