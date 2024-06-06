import json
from difflib import get_close_matches
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone

recognizer = Recognizer()
engine = init()
engine.runAndWait()
voices = engine.getProperty("voices")

def speak(text):
    engine.say(text)
    engine.runAndWait()
    text=list(text)

def load_conoscenze(file_path: str):
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data
def save_conoscenza(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
    
def find_migliore_risposta(user_question: str, question :list[str]): 
    match: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return match[0] if match else None
def get_prendi_la_risposta(question: str, conoscenze: dict):
    for q in conoscenze["domande"]:
        if q["domanda"] ==question:
            return q["risposta"]
def chat_bot():
    conoscenze: dict= load_conoscenze("conoscenze.json")

    while True:
        with Microphone() as source:
            print("Ascoltando...")
            speak("sto ascoltando")
            audio = recognizer.listen(source)
            user_input: str = audio

        if user_input.lower()=="esci":
            break
        
        migliore_risposta: str | None = find_migliore_risposta(user_input, [q["domanda"] for q in conoscenze["domande"]])

        if migliore_risposta:
            risposta: str  = get_prendi_la_risposta(migliore_risposta, conoscenze)
            speak(f"{risposta}")
        
        else:
            speak(" non conosco la risposta insegnami")
            speak("dammi una risposta pls opure deprimimi e scrivi 'skip': ")
            nuova_risposta: str = user_input

            if nuova_risposta.lower() != "skip":
                conoscenze["domande"].append({"domanda": user_input, "risposta":nuova_risposta})  
        

                save_conoscenza("conoscenze.json", conoscenze)
                speak(" grazie puccio")


        
if __name__=="__main__":
    chat_bot()