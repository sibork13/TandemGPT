import pyttsx3

class Text_Voice():
    def __init__(self):
        # Inicializar el motor de síntesis de voz
        self.engine = pyttsx3.init()

        # Configurar la velocidad de la voz
        self.engine.setProperty('rate', 150)   # Velocidad de 150 palabras por minuto

        # Configurar el volumen de la voz
        self.engine.setProperty('volume', 0.7) # Volumen al 70% (valor entre 0 y 1)
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0')

    def TtV_converter(self,text):
        self.engine.say(text)
        self.engine.runAndWait()