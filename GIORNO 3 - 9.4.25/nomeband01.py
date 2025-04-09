'''
Scrivere un programma in Python che genera un nome per una band musicale utilizzando due input forniti
dall'utente: la città di origine e il nome del proprio animale domestico
'''


#generiamo il nome della città e dell'animale
citta = input("Inserisci il nome della citta ")
animale = input ("Inserisci il nome dell'animale ")

#generiamo il nome della band
nome_band = f"{citta} {animale}"

#Mostriamo il risultato
print(f"Il nome della band che hai generato è il seguente: {nome_band}")