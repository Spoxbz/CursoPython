#4.- Adivina el número: escribe un programa que genere un número aleatorio y que permita al usuario adivinar cuál es. Proporcionar pistas como “Demasiado alto” y “Demasiado bajo” hasta que el usuario adivine el número.

import random

def number_guess():
    random_number = random.randint(10, 20)

    while True:
        riddle = int(input("Ahora tienes que adivinar un número(entre 10 y 20): "))

        if riddle == random_number:
            print(f"¡Felicidades! Adivinaste, el número era: ", random_number)
            break
        elif riddle < random_number:
            print("Demasiado bajo. Intenta de nuevo.")
        else:
            print("Demasiado alto. Intenta de nuevo.")

# Iniciar el juego
number_guess()