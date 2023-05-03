import os
import openai
from secret_key import API_KEY
import json



# loading the API key from the secret_key file
openai.api_key = API_KEY

class chatgpt():
    def __init__(self):
        self.model = 'text-davinci-003'
        self.temperature = 0.9
        self.max_tokens = 50
        self.top_p = 1
        self.frecuency_penalty = 0.5
        self.precence_penalty = 0.0
        self.stop = ['you:']

    def chat(self,message):
        response = openai.Completion.create(
            model=self.model,
            prompt=message,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frecuency_penalty,
            presence_penalty=self.precence_penalty
        )
        response = self.format_response(response)

        return response
    
    def format_response(self,response):
        response = str(response)
        response = json.loads(response)["choices"][0]["text"]
        response = response.replace('friend:','').replace('\n','')
        return response