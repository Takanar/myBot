import speech_recognition as sr
import pyttsx3



def falar(palavra):
    en = pyttsx3.init()
    en.setProperty('voice',b'brazil')

    en.say(palavra)

    en.runAndWait()

def ouvir():
    rec = sr.Recognizer()
    with sr.Microphone() as fala:
        frase = rec.listen(fala)
        try:
            vfala = rec.recognize_google(frase, language="pt")
            print(vfala)
            
        except:
            print("Não entendi")
            falar('nao entendi')

while True:
    ouvir()

