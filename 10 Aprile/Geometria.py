figura = input("inserisci figura : ")

if figura == "Quadrato":
    try:
     lato = int(input("Metti valore lato quadrato : "))
     calcolo_perimetro = lato * 4
     print(f"Il valore del perimetro del quadrato e : {calcolo_perimetro}")
    except ValueError:
        print("Serve un numero")


elif figura == "Cerchio":
    try:
     raggio = int(input("Metti valore raggio : "))
     pi_greco = 3.14
     calcolo_circonferenza = 2 * pi_greco * raggio
     print(f"Il valore della circoferenza e : {calcolo_circonferenza}")
    except ValueError:
     print("Serve un numero")

elif figura == "Rettangolo":
    try:
     base=int(input("Inserisci base"))
     altezza=int(input("Inserisic altezza"))
     calcolo_perimetro= base*altezza / 2
     print(f"Il perimetro e : {calcolo_perimetro}")
    except ValueError:
        print("Serve un numero")

else :
    print("Bisogna inserire il nome della figura")    

