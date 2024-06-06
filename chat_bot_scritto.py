import json
from difflib import get_close_matches


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
        user_input: str = input("you: ")

        
        
        migliore_risposta: str | None = find_migliore_risposta(user_input, [q["domanda"] for q in conoscenze["domande"]])

        if migliore_risposta:
            risposta: str  = get_prendi_la_risposta(migliore_risposta, conoscenze)
            print(f"bot: {risposta}")
        else:
            print("Bot: non conosco la risposta insegnami")
            nuova_risposta: str = input("dammi una risposta pls opure deprimimi e scrivi 'skip': ") 

            if nuova_risposta.lower() != "skip":
                conoscenze["domande"].append({"domanda": user_input, "risposta":nuova_risposta})  
        

                save_conoscenza("conoscenze.json", conoscenze)
                print("Bot: grazie puccio")


        
        if user_input.lower()=="esci" or risposta.lower()=="ciao ciao":
            break
        
        if user_input.lower()=="posso insegnarti qualcosa?":
            print("si dimmi la domanda: ")
            nuova_risposta: str = input("dammi una risposta pls opure deprimimi e scrivi 'skip': ")
            conoscenze["domande"].append({"domanda": user_input, "risposta":nuova_risposta})
if __name__=="__main__":
    chat_bot()