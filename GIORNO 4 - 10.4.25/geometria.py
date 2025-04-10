import math
#CREA FUNZIONE
def calcola_perimentro():
    while True:
        print("\nScegli una figura geometrica:")
        print("1. Quadrato")
        print("2. Cerchio")
        print("3. Rettangolo")
        print("4. Esci dal programma")
#CREA LA SCELTA
        scelta = input("Inserisci il numero corrispondente alla figura:")
#CALCOLO QUADRATO
        if scelta == "1":
            lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
            perimetro = 4 * lato 
            print(f"Il perimetro del quadrato è: {perimetro}")
#CALCOLO CERCHIO
        elif scelta == "2":
            raggio = float(input("Inserisci il raggio del cerchio: "))
            circonferenza = 2* math.pi * raggio
            print((f"La circonferenza del cerchio è: {circonferenza}"))
#CALCOLO RETTANGOLO
        elif scelta == "3":
            base = float(input("Inserisci la base del rettangolo: "))
            altezza = float(input("Inserisci l'altezza del rettangolo: "))
            perimetro = 2 * (base + altezza)
            print(f"Il perimetro del rettangolo è: {perimetro}")
#CHIUDERE IL PROGRAMMA      
        elif scelta == "4":
            print("Esci dal programma.") 
            break
#CONTROLLO     
        else:
            print("Scelta non valida. Riprova.")
calcola_perimentro()