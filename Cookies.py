import os
import json
import base64
import sqlite3
import shutil
from datetime import datetime, timedelta
import win32crypt # pip install pypiwin32
from Crypto.Cipher import AES # pip install pycryptodome
import csv
from os import remove


class Cookie_extractor():
    def __init__(self):
        self.site_cookies_list = list()



    def get_chrome_datetime(self,chromedate):
        """Return a `datetime.datetime` object from a chrome format datetime
        Since `chromedate` is formatted as the number of microseconds since January, 1601"""
        if chromedate != 86400000000 and chromedate:
            try:
                return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except Exception as e:
                print(f"Error: {e}, chromedate: {chromedate}")
                return chromedate
        else:
            return ""

    def get_encryption_key(self):
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        # decode the encryption key from Base64
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        # remove 'DPAPI' str
        key = key[5:]
        # return decrypted key that was originally encrypted
        # using a session key derived from current user's logon credentials
        # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    
    def decrypt_data(self,data, key):
        try:
            # get the initialization vector
            iv = data[3:15]
            data = data[15:]
            # generate cipher
            cipher = AES.new(key, AES.MODE_GCM, iv)
            # decrypt password
            return cipher.decrypt(data)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except:
                # not supported
                return ""

    def extractor(self,site):

        # local sqlite Chrome cookie database path
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
        # copy the file to current directory
        # as the database will be locked if chrome is currently open
        filename = "Cookies.db"
        if not os.path.isfile(filename):
            # copy file when does not exist in the current directory
            shutil.copyfile(db_path, filename)
        # connect to the database
        db = sqlite3.connect(filename)
        # ignore decoding errors
        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()
        # get the cookies from `cookies` table using certain domain
        cursor.execute(f"""
        SELECT host_key, value, is_httponly, path, is_secure, expires_utc, name, encrypted_value
        FROM cookies
        WHERE host_key like '%{site}%'""")
        # get the AES key
        key = self.get_encryption_key()
        for host_key,value, is_httponly, path, is_secure, expires_utc, name, encrypted_value in cursor.fetchall():
            if path == '/':
                decrypted_value = self.decrypt_data(encrypted_value, key)
                cookies_list = [host_key, is_httponly, path, is_secure, expires_utc, name, decrypted_value]
                self.site_cookies_list.append(cookies_list)
        # close connection
        db.close()
        remove(filename)
        return self.site_cookies_list
    
    def get_cookies_txt(self,site):
        data = self.extractor(site)
        with open('cookies.txt', 'w') as f:
            for row in data:
                line = ' '.join(str(x) for x in row) + '\n'
                line = line.replace(' ','	')
                f.write(line)