import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# install("googletrans")
# install("pywhatkit")
# install("speechRecognition")
# install("pyAudio")
# install("google-generativeai")
# install("pydub")
# install("gTTS")
# install("playsound==1.2.2")
install("whatsapp-api-client-python")
    
    
