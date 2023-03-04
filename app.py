import random
import string
import pyfiglet
import time
from art import text2art
from colorama import init, Fore, Back, Style
#Variabili
utilizzo = None
# Inizializza colorama
init()

text = pyfiglet.figlet_format("Generatore di Password\n by Infinity Studios Inc.")
print(text)

def generate_password(length):
    # Scelta dei caratteri possibili per la password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generazione della password casuale
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Esempio di utilizzo

lunghezza = int(input("Di quanti caratteri deve essere lunga la password?\n"))
password = generate_password(lunghezza)
print("Password generata " + Fore.GREEN + "con successo!" + Fore.WHITE + '\n' + Back.RED + password + Back.BLACK)

with open('Password.txt', 'w') as file:
    # Scrivi nel file
    file.write('Questo è un esempio di testo.\n')
    file.write('Puoi aggiungere quante righe vuoi.\n')

daCapo = input("Vuoi generare un'altra Password? [s/n]\n")
if(daCapo == "n"):
    exit()

    
while daCapo == "s":
    lunghezza = int(input("Di quanti caratteri deve essere lunga la password?\n"))
    password = generate_password(lunghezza)
    print("Password generata " + Fore.GREEN + "con successo!" + Fore.WHITE + '\n' + Back.RED + password + Back.BLACK)

    with open('Password.txt', 'w') as file:
        # Scrivi nel file
        file.write('Questo è un esempio di testo.\n')
        file.write('Puoi aggiungere quante righe vuoi.\n')

    daCapo = input("Vuoi generare un'altra Password? [s/n]\n")
    if(daCapo == "n"):
        exit()








