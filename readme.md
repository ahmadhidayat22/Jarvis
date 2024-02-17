# About
  python speech recognition with Gemini AI
  
# Installation

### For windows users
  for the program to listen to our voice/speech `pip install speechRecognition`, for more details https://pypi.org/project/SpeechRecognition/
  
  you maybe need a pyaudio, so ```pip install pyAudio```
  
  to speak up, or text to speech ```pip install pyttsx3```
  
  and exciting thins, Gemini AI  ```pip install -q -U google-generativeai```

# Usage
  make sure all library are, then change the token ```BARD_API``` in ```.env``` with your api key that you have registered, if not you can create an api key first in https://makersuite.google.com.
  then run a program  ```python main.py```
  
  
## Requirement
  - Python 3.8+ (required)
  - PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
  - PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
  - Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
  - Gemini api key https://makersuite.google.com/app or other

<br>


> [!NOTE]
> this is a beta program, the script will be updated soon
