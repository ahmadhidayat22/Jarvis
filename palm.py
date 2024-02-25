import google.generativeai as genai
from dotenv import load_dotenv , find_dotenv
import os




load_dotenv(find_dotenv())
API_KEY= os.getenv('BARD_API')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('chat-bison-001')


text= input("You :")
# Create a new conversation
response = genai.chat(messages=text , temperature=1)

# Last contains the model's response:
print(response.last)

while True:
    text= input("You :")
    response= response.reply(text)

    print(f'\n{response.last}')