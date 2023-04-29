from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Webdriver():
    def __init__(self,url):
        self.options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=self.options)
        self.url = url



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
        print (cookies)
        self.driver.get(self.url)
        time.sleep(2)
        print(self.driver.get_cookies())
        # adding cookies
        for c in cookies:
            self.driver.add_cookie(c)
        print ('')
        print ('[+] Added cookies')
        print(self.driver.get_cookies())
        self.driver.get(self.url)
        time.sleep(30)
    