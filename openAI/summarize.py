import openai
import requests 
from mySecrets import getOpenAIKey

# Set the API key
openai.api_key = getOpenAIKey()

def chatGptDavinci002(rawText):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="summarize: " + rawText,
        max_tokens=4000,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    summary = response["choices"][0]["text"]
    #summary = response.text
    return summary

def getSummary(rawText_list):
    data = ""
    for rawText in rawText_list:
        data += chatGptDavinci002(rawText) + " "
    return data

#getSummary("hello and hi")    

def getSummary2(text):
    url = "https://api.openai.com/v1/completions"
    request_body = {
        "model": "text-davinci-003",
        "prompt": "Please summarize the following raw text in a few paragraphs:\n" + text,
        "max_tokens": 100,
        "temperature": 0.5,
        }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + getOpenAIKey()
        }

    response = requests.post(url, json=request_body, headers=headers)
    jsonRes = response.json()
    print(jsonRes["choices"][0]["text"])
