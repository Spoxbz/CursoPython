# 6.- Generador de contraseñas: escribe un programa que genere una contraseña aleatoria de una longitud especificada por el usuario. Esta debe contener letras, números, y caracteres especiales. 

# la variable 'set' estoy usandola para referirme al conjunto de de todos los caracteres para formar la contraseña
import random
import string

def generar_contrasena(pass_length):
    # Definir los conjuntos de caracteres para la contraseña
    lower_letters = string.ascii_lowercase
    uppers_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Combinar los conjuntos de caracteres en uno solo
    set = lower_letters + uppers_letters + numbers + symbols

    # Generar la contraseña aleatoria
    password = "".join(random.choice(set) for _ in range(pass_length))

    return password

# Solicitar la longitud de la contraseña al usuario
pass_length = int(input("Ingrese la longitud deseada para la contraseña: "))

# Generar y mostrar la contraseña
generated_pass = generar_contrasena(pass_length)
print(f"Su contraseña aleatoria es: {generated_pass}")
