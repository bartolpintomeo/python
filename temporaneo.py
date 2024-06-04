from deepface import DeepFace
import copy

def speak(message):
    print(message)  # Replace this with actual text-to-speech implementation

def identify_person(img, references):
    try:
        for name, ref in references.items():
            if DeepFace.verify(img, ref)["verified"]:
                return name
    except ValueError:
        return None

# Define your reference images
referenceb = {"path/to/referenceb/image"}
referenced = {"path/to/referenced/image"}
referencem = {"path/to/referencem/image"}

# Dictionary of references
references = {
    "bartolomeo": referenceb.copy(),
    "dottore": referenced.copy(),
    "maestro": referencem.copy(),
}

# Process the image
img = "path/to/input/image"  # Replace with the actual input image
person = identify_person(img, references)

if person == "bartolomeo":
    speak("Ciao Bartolomeo, cosa posso fare per te?")
elif person == "dottore":
    speak("Ciao Dottore, cosa posso fare per te? Mi è piaciuta la mega sborrata di ieri, adoro il tuo sesso selvaggio.")
elif person == "maestro":
    speak("Ciao Maestro, sei veramente un gran figo, ti va di fare sesso?")
else:
    speak("Chi sei?")

# Continuously listen for audio input
import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

# Dictionary of insults and responses
risposte_insulti = {
    "insulto1": "risposta1",
    "insulto2": "risposta2",
    # Add more insults and responses as needed
}

while True:
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            testo = recognizer.recognize_google(audio, language="it-IT").lower()
            print("Hai detto:", testo)
            
            # Check for insults in the recognized text and respond accordingly
            risposta = None
            for insulto, risposta_ in risposte_insulti.items():
                if insulto in testo:
                    risposta = risposta_
                    break

            if risposta:
                speak(risposta)
            else:
                speak("Non ho capito cosa hai detto.")
        except sr.UnknownValueError:
            speak("Non ho capito cosa hai detto.")
        except sr.RequestError as e:
            speak(f"Errore nel servizio di riconoscimento vocale: {e}")
