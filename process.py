from VoiceText import Voice_Text
from TextVoice import Text_Voice
from chatbot import chatgpt

TV = Text_Voice()
VT = Voice_Text()
gpt = chatgpt()

initial_prompt = "You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:"
prompt = ''
if __name__ == '__main__':
    try:
        response = gpt.chat(initial_prompt)
        TV.TtV_converter(response)
        #prompt = 'you' + VT.VtT_converter()
        '''
        while prompt != 'exit':
            prompt = 'you' + VT.VtT_converter()
            print(prompt)
            response = gpt.chat(prompt)
            TV.TtV_converter(response)
        '''
        


    except Exception as ex:
        print ('[!] Error: {}'.format(ex))
    finally: print ('[+] Finished !')


