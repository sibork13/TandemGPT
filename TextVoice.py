import pyttsx3

class Text_Voice():
    def __init__(self,language_path,volume,wpm):
        # Start voice synthesiser
        self.engine = pyttsx3.init()

        # Set words per minute
        self.engine.setProperty('rate', wpm) 

        # Set volume
        self.engine.setProperty('volume', volume) # (value between 0 and 1)
        self.engine.setProperty('voice', language_path)

    def TtV_converter(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
        