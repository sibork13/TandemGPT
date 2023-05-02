from Cookies import Cookie_extractor
from VoiceText import Voice_Text
from web_driver import Webdriver
from TextVoice import Text_Voice


# getting cookies
#site = '.twitch.tv'
site = '.openai.com'
CO = Cookie_extractor()
CO.get_cookies_txt(site)

# importing cookies to webdriver
#site_url = 'https://www.twitch.tv/'
#site_url = 'https://chat.openai.com/'

site_url ='your_url'
wb = Webdriver(site_url)
TV = Text_Voice()
VT = Voice_Text()
first_text = 'あなたが私に与える各答えの最後にSAIGOという言葉を入れてください. 例：皆様のご来場、お待ちしています SAIGO'
text = ''


if __name__ == '__main__':
    try:
        
        wb.open_with_cookies()
        print('Webdriver opened')
        wb.Open_Chat()
        print('Chat opened')
        wb.start_chat(first_text)
        print('Starting chat')
        first_response = wb.read_response()
        TV.TtV_converter(first_response)
        while True:
            # Converting voice to text
            text = input('Enter voice text')
            if text != 'エンドチャット':
                wb.send_message(text)
                # waiting for response
                wb.read_response()
                # Converting response to voice
                TV.TtV_converter(text)
            else:
                break



    except Exception as ex:
        print ('[!] Error: {}'.format(ex))
    finally: print ('[+] Finished !')

    wb.close_driver()

