import cv2
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from deepface import DeepFace

# Dizionario di insulti e risposte corrispondenti
risposte_insulti = {
    "regolare": "Sei così imbarazzante che fai arrossire gli specchi.",
    "stefano": "stefano, scaricati tik tok, altrimenti ti inculo",
    "dottore": "dottore, le vorrei sborrare in testa",
    "tomas": "tomas e gay",
    "yao": "yao vieni ora a casa mia sul leto",
    "tristana": "levati dalle palle",
    "lux": "lux brucia",
    "aurora": "guarda un cane",
    "ale": "vieni su lol?",
    "alem": "vieni ora su lol",
    "prof": "prof ugo ha da crepà"
}

# Inizializzazione del motore di text-to-speech
engine = init()
engine.runAndWait()
voices = engine.getProperty("voices")

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

references = {
    "bartolomeo": cv2.imread("riferimento.jpg"),
    "dottore": cv2.imread("riferimento3.jpg"),
    "maestro": cv2.imread("riferimento4.jpg"),
}

recognizer = Recognizer()

# Funzione per far parlare il motore
def speak(text):
    engine.say(text)
    engine.runAndWait()

def identify_person(img, references):
    try:
        min_distance = float('inf')
        identified_person = None

        for name, ref in references.items():
            distance = DeepFace.verify(img, ref)["distance"]
            if distance < min_distance:
                min_distance = distance
                identified_person = name

        if min_distance < 0.6:  # Esempio di soglia di similarità
            return identified_person
        else:
            return None

    except ValueError:
        return None

def recognize_and_respond():
    with Microphone() as source:
        print("Ascoltando...")
        audio = recognizer.listen(source)

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
                person = identify_person(img, references)
                try:
                    if person:
                        if person == "bartolomeo":
                            speak("Ciao Bartolomeo, cosa posso fare per te?")
                        elif person == "dottore":
                            speak("Ciao Dottore, cosa posso fare per te? Mi è piaciuta la mega sborrata di ieri, adoro il tuo sesso selvaggio.")
                        elif person == "maestro":
                            speak("Ciao Maestro, sei veramente un gran figo, ti va di fare sesso?")
                    else:
                        speak("Chi sei?")
                except ValueError:
                    speak("Chi sei?")

                while True:
                    audio = recognizer.listen(source)
                    testo = recognizer.recognize_google(audio, language="it-IT").lower()
                    print("Hai detto:", testo)

                    # Controllo se c'è un insulto nel testo riconosciuto e risponde di conseguenza
                    risposta = None
                    for insulto, risposta_ in risposte_insulti.items():
                        if insulto in testo:
                            risposta = risposta_
                            break

                    if risposta:
                        speak(risposta)
                    else:
                        speak("Non ho capito cosa hai detto.")

            # Se non viene pronunciata l'attivazione, continua ad ascoltare
            else:
                recognize_and_respond()

        except Exception as e:
            print("Errore nel riconoscimento vocale:", e)
            speak("Errore nel riconoscimento vocale.")
            recognize_and_respond()

# Avvia la funzione per gestire il riconoscimento vocale e la risposta agli insulti
recognize_and_respond()
