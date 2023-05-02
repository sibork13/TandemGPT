import pyttsx3
import speech_recognition as sr
import difflib


class Voice_Text():
    def __init__(self):
        # Configurar el reconocedor de voz
        self.r = sr.Recognizer()


    def VtT_converter(self):
        # Escuchar la respuesta del usuario y transcribirla
        print('Please say something')
        with sr.Microphone(device_index=4) as source:
            audio = self.r.listen(source)

        try:
            transcription = self.r.recognize_sphinx(audio)
            print("Transcription: " + transcription)
        except sr.UnknownValueError:
            print("Unable to transcribe audio")
        return transcription