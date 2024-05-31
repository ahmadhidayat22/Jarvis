# About
  Python speech recognition with Gemini AI
  
# Installation

### For windows users
  for the program to listen to our voice/speech `pip install speechRecognition`, for more details https://pypi.org/project/SpeechRecognition/
  
  you maybe need a pyaudio, so ```pip install pyAudio```
  
  to speak up, or text to speech ```pip install pyttsx3```

  to play a sound when listening , ```pip install pydub```  and you may need a ffmpeg, i use this https://www.gyan.dev/ffmpeg/builds/packages/ffmpeg-6.1.1-full_build.7z
  
  and exciting thing, Gemini AI  ```pip install -q -U google-generativeai```
> [!NOTE]
> kamu bisa install package secara langsung dengan menjalankan [installpip.py](https://github.com/ahmadhidayat22/Jarvis/blob/main/installpip.py)


# Usage
  make sure all library are, then change the token ```BARD_API``` in ```.env``` with your api key that you have registered, if not you can create an api key first in https://makersuite.google.com. And ```WEATHER_KEY``` with your api weather, you can get this in https://api.openweathermap.org.
  
  then run the program 
  
  
## Requirement
  - Python 3.8+ (required)
  - PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
  - PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
  - Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
  - Gemini api key https://makersuite.google.com/app or other

<br>


> [!NOTE]
> this is a beta program, the script will be updated soon
