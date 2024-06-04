from pyttsx3 import init
from speech_recognition import Recognizer, Microphone

# Dizionario di insulti e risposte corrispondenti
risposte_insulti = {
    "regolare": "Sei così imbarazzante che fai arrossire gli specchi.",
    "stefano": "stefano, ti vengo ad inculare con vadim",
    "dottore": "dottore, le vorrei sborrare in testa",
    "tomas":"tomas e gay",
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
# for voice in voices:
#     print(voice)

# Inizializzazione del riconoscimento vocale
recognizer = Recognizer()

# Funzione per far parlare il motore
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Funzione per gestire il riconoscimento vocale e la risposta agli insulti
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
                speak("Sì, cosa posso fare per te?")
                # Dopo aver riconosciuto l'attivazione, continua ad ascoltare per ulteriori input vocali
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