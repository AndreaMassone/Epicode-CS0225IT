import datetime 
def assistente_virtuale(comando):
    #Per fare in modo che l'utente possa utlizzare il programma
    #in maniera meno "rigida" possiamo aggiungere la sintassi .lower() e .strip() :
    if comando == "Qual è la data di oggi?":
        # Il modulo datetime.datetoday non esiste.
        # La correzione dobrebbe essere : datetime.date.today()
        oggi = datetime.datetoday()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L ora attuale è" + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"   
    else:
        risposta = "Non ho capito la tua domanda?"
        return risposta   
    #Dopo il Treu mancano i due punti :                                                
while True 
    comando_utente = input("Cosa vuoi sapere?")
    if comando_utente.lower() == "esci" :
      print("Arrivederci!")
      break
    else:
       print(assistente_virtuale(comando_utente))
