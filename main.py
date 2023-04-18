import pyttsx3
import requests as fetch
import json
import openai

chatgpt_key = "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"

endpoint = 'https://api.openai.com/v1/models'
openai.organization = "org-Tae2Fv5yn1I2nefY3BwPM2Tk"
openai.api_key = chatgpt_key
openai.Model.list()

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {chatgpt_key}'
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

# print(endpoint, headers, data)
# api_response = fetch.post(endpoint, headers=headers, json=data)
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
text = input('Hey what can I do for you today? ')

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": text}
    ]
)

chatgpt_response = response['choices'][0]['message']['content']

# print('from 26', api_response.status_code)
# print('from 27', api_response.json)

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 2)

print(chatgpt_response)
engine.say(chatgpt_response)

# Run and wait for the speaking to finish
engine.runAndWait()
