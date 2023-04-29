from Cookies import Cookie_extractor
from VoiceText import Voice_Text as VC
from web_driver import Webdriver



# getting cookies
#site = '.twitch.tv'
site = '.openai.com'
CO = Cookie_extractor()
CO.get_cookies_txt(site)

# importing cookies to webdriver
#site_url = 'https://www.twitch.tv/'
site_url = 'https://chat.openai.com/'
wb = Webdriver(site_url)
try:
    wb.open_with_cookies()
except Exception as ex:
    print ('[!] Error: {}'.format(ex))
finally: print ('[+] Finished !')

wb.close_driver()

