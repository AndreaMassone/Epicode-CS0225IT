import datetime 

def assistente_virtuale(comando):
    comando = comando.lower().strip()

    if comando == "qual è la data di oggi?":
        oggi = datetime.date.today()
        risposta = "la data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "l ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"   
    else:
        risposta = "Non ho capito la tua domanda"
    return risposta  

def opzioni():
  print("Scegli uno delle opzioni disponibili")  
  print("Qual è la data di oggi")  
  print("Qual è l'ora attuale") 
  print("Puoi chidere il mio nome")

print("Ciao sono il programma Assistente Virtuale\nCosa vuoi sapere?")
opzioni()
while True :
    comando_utente = input("Se hai gia tutte le tue risposte digita esci\n")
    if comando_utente.lower() == "esci" :
       print("Arrivederci!")
       break
    else:
       print(assistente_virtuale(comando_utente))
