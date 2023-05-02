from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# library to help bypass cloudflare bot detector
from selenium_stealth import stealth
import time

class Webdriver():
    def __init__(self,url):
        self.options = Options()
        self.options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')
        self.options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=self.options)
        self.url = url
        # bypass cloudflare 
        stealth(self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )



    def open_driver(self):
        self.driver.get(self.url)

    def close_driver(self):
        self.driver.quit()

    
    def read_cookies(self,p = 'cookies.txt'):
        # read cookies from file
        # format
        # ... expiry1 key1 value1
        # ... expiry2 key2 value2
        cookies = []
        with open(p, 'r') as f:
            for e in f:
                e = e.strip()
                if e.startswith('#'): continue
                k = e.split('	')
                if len(k) < 3: continue	# not enough data
                cookies.append({'host_key': k[0],'is_httponly':int(k[1]),'path':k[2],'is_secure':int(k[3]), 'expires_utc': int(k[4]), 'name':k[5], 'value': k[6]})
        return cookies  
    
    
    def open_with_cookies(self):
        # import cookies into selenium webdriver (to bypass authenticate)
        cookies = self.read_cookies()
        print ('[+] Read {} cookies'.format(len(cookies)))
        ##print (cookies)
        self.driver.get(self.url)
        #self.driver.maximize_window()
        time.sleep(3)
        print(';AS COOKIES DEL BOT SON\n\n')
        #print(self.driver.get_cookies())
        # adding cookies
        for c in cookies:
            self.driver.add_cookie(c)
        print ('')
        print ('[+] Added cookies')
        ##print(self.driver.get_cookies())
        self.driver.get(self.url)
        #time.sleep(10)
    
    def Open_Chat(self):
        time.sleep(2)
        next = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button')
        next.click()
        time.sleep(1)
        next = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]')
        next.click()
        time.sleep(2)
        done = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]')
        done.click()
        # find chat
        time.sleep(3)

    

    def start_chat(self,first_text):
        #first_text = "こんにちは、私は日本語を勉強しているので、私の編集に誤りがあれば教えてください。"
        # find text box and send text
        self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea').send_keys(first_text + Keys.ENTER)
        # wait until full response are received
        WebDriverWait(self.driver, 19).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def send_message(self,message):
        # waiting 1 second to send message
        #time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea').send_keys(message + Keys.ENTER)
        time.sleep(300/1000)
        
    
    def read_response(self):
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, '//div[@class="group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]"][last()]/div/div[2]/div[1]/div/div/p[last()]'),'SAIGO')) #Find element by text
        #WebDriverWait(self.driver, 19).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        answer = self.driver.find_elements(By.XPATH,'//div[@class="group w-full text-gray-800 dark:text-gray-100 border-b border-black/10 dark:border-gray-900/50 bg-gray-50 dark:bg-[#444654]"][last()]/div/div[2]/div[1]/div/div/p')
        answer = [tag.text for tag in answer]
        answer = '. \n'.join(answer)
        # BUSCAR EXTRAER TODA LA RESPUESTA  PARA IMPRIMIRLA
        return answer