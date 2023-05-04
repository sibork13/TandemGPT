from VoiceText import Voice_Text
from TextVoice import Text_Voice
from chatbot import chatgpt
import json

config = json.loads("Config.json")["Default"]

initial_prompt = config["initial_prompt"]
bot_name = config["bot_name"]
model = config["model"]
prompt = config["prompt"]
language_path = config["language_path"]
volume = config["volume"]
wpm = config["wpm"]

TV = Text_Voice(language_path,volume,wpm)
VT = Voice_Text()
gpt = chatgpt(model)


if __name__ == '__main__':
    try:
        response = gpt.chat(initial_prompt,bot_name)
        TV.TtV_converter(response)
        
        while prompt != 'exit':
            prompt = 'you: ' + VT.VtT_converter()
            print(prompt)
            response = gpt.chat(prompt,bot_name)
            TV.TtV_converter(response)
        
        

        print(prompt)
    except Exception as ex:
        print ('[!] Error: {}'.format(ex))
    finally: print ('[+] Finished !')


