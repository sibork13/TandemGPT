from VoiceText import Voice_Text
from TextVoice import Text_Voice
from chatbot import chatgpt


TV = Text_Voice()
VT = Voice_Text()
gpt = chatgpt()

initial_prompt = "You: What have you been up to?\nFriend: listening japanese music.\nYou: Did you listen anything interesting?\nFriend:"

#initial_prompt = "The following is a conversation with japanese friend, all conversation will be on japanese.\nyou:ね、ししゃものことを聞きますか\nfriend: 新しいアルバムのこと？\nyou:うん、めっちゃいいでしょう？"
prompt = ''

if __name__ == '__main__':
    try:
        response = gpt.chat(initial_prompt)
        TV.TtV_converter(response)
        #prompt = 'you: ' + VT.VtT_converter()
        
        while prompt != 'exit':
            prompt = 'you: ' + VT.VtT_converter()
            print(prompt)
            response = gpt.chat(prompt)
            TV.TtV_converter(response)
        
        

        print(prompt)
    except Exception as ex:
        print ('[!] Error: {}'.format(ex))
    finally: print ('[+] Finished !')


