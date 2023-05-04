import speech_recognition as sr



class Voice_Text():
    def __init__(self):
        # Configuring the speech recogniser
        self.r = sr.Recognizer()


    def VtT_converter(self):
        # Listen to the user's response and transcribe it.
        print('Please say something')
        with sr.Microphone(device_index=4) as source:
            audio = self.r.listen(source)

        try:
            print('End of recording')
            transcription = self.r.recognize_sphinx(audio)
            print("Transcription: " + transcription)
            return transcription
        except sr.UnknownValueError:
            print("Unable to transcribe audio")
        
    