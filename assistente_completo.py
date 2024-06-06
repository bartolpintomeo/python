import cv2
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
import numpy as np
from deepface import DeepFace
import pygame
import time
from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

giocatori=read_csv("giocatori.csv")
X=giocatori.drop(columns=["videogame"])
y=giocatori["videogame"]
modello=DecisionTreeClassifier()
modello.fit(X.values, y.values)
pygame.init()

area=pygame.display.set_mode((500,500))
i=0
area.fill((255,255,255))
face=300
eyes=250
raggio=100
raggiom=raggio
rect=pygame.Rect((200,280), (raggio+20, raggiom))

# Dizionario di insulti e risposte corrispondenti
risposte_insulti = {
    "regolare": "Sei così imbarazzante che fai arrossire gli specchi.",
    "stefano": "stefano, ti vengo ad inculare con Vadim",
    "dottore": "dottore, le vorrei sborrare in testa",
    "thomas":"tomas è gay",
    "yao":"yao vieni ora a casa mia sul leto",
    "tristana":"levati dalle palle",
    "lux":"lux brucia",
    "aurora":"guarda un cane",
    "ale":"vieni su lol?",
    "alem":"vieni ora su lol",
    "prof":"prof ugo ha da crepà"    
    }

# Inizializzazione del motore di text-to-speech
engine = init()
engine.runAndWait()
voices = engine.getProperty("voices")
referenceb=cv2.imread("immagini/bartolomeo.jpg")
referenced=cv2.imread("immagini/dottore.jpg")
referencem=cv2.imread("immagini/maestro.jpg")
referencef=cv2.imread("immagini/francesco.jpg")
referenceste=cv2.imread("immagini/stefano.jpg")

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)



recognizer = Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()
    text=list(text)

def identify_person(img, references):
    try:
        for name, ref in references.items():
            if DeepFace.verify(img, ref)["verified"]:
                return name
    except ValueError:
        return None


def recognize_and_respond():
    with Microphone() as source:
        print("Ascoltando...")
        speak("sto ascoltando")
        audio = recognizer.listen(source

        try:
            # Riconoscimento vocale utilizzando Google (senza configurazione delle credenziali)
            testo = recognizer.recognize_google(audio, language="it-IT").lower()
            print("Hai detto:", testo)

            # Controllo se viene pronunciata l'attivazione
            if "ciao giovanna" in testo:
                    ret, img = cap.read()
                    img = cv2.flip(img, 1)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(
                        gray,     
                        scaleFactor=1.2,
                        minNeighbors=5,     
                        minSize=(20, 20)
                    )
                    
                    references = {
                        "bartolomeo": referenceb.copy(),
                        "dottore" : referenced.copy(),
                        "maestro" : referencem.copy(),
                        "francesco" : referencef.copy(),
                        "stefano" : referenceste.copy(),
                        }
                    person = identify_person(img, references)
                    try:
                        if person == "bartolomeo":
                            speak("Ciao Bartolomeo, cosa posso fare per te?")
                        elif person == "dottore":
                            speak("Ciao dottore, cosa posso fare per te?Mi è piaciuto il sesso selvaggio di ieri")
                        elif person == "maestro":
                            speak("Ciao maestro, cosa posso fare per te?Scopami il culo ")
                        elif person == "francesco":
                            speak("Ciao francesco, cosa posso fare per te?")
                        elif person == "stefano":
                            speak("Ciao stefano, cosa posso fare per te?")
                    except ValueError:
                                    speak("chi sei?")
            while True:
                        audio = recognizer.listen(source)
                        testo = recognizer.recognize_google(audio, language="it-IT").lower()
                        print("Hai detto:", testo)

                        if testo=="consigliami un gioco":
                            speak("dimmi la tua età")
                            eta=testo
                            speak("dimmi, cosa hai nelle mutande?")
                            sesso=testo
                            try:
                                if sesso=="maschio":
                                    sesso=1
                                elif sesso=="femmina":
                                    sesso=0
                                else:
                                    speak("non ho capito")
                                
                                previsioni = modello.predict([[sesso, eta]])
                                speak(previsioni)
                            except ValueError:
                                 speak("non ho capito")
                        # Controllo se c'è un insulto nel testo riconosciuto e risponde di conseguenza
                        risposta = None
                        for insulto, risposta_ in risposte_insulti.items():
                            if insulto in testo:
                                risposta = risposta_
                                break

                        if risposta:
                            speak(risposta)

                        elif  "ciao giovanna" in testo:
                            ret, img = cap.read()
                            img = cv2.flip(img, 1)
                            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                            faces = faceCascade.detectMultiScale(
                                gray,     
                                scaleFactor=1.2,
                                minNeighbors=5,     
                                minSize=(20, 20)
                            )
                        else:
                            speak("Non ho capito cosa hai detto.")
                            

            # Se non viene pronunciata l'attivazione, continua ad ascoltare
            else:
                recognize_and_respond()

        except Exception as e:
            print("Errore nel riconoscimento vocale:", e)
            speak("Errore nel riconoscimento vocale.")
            recognize_and_respond()

recognize_and_respond()