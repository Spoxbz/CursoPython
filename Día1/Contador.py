# 3.- Contador de palabras: escribe un programa que cuente el número de palabras en una cadena de texto dada.
sentence = input("Ingrese una oracion: ")
words = sentence.split()
count = 0

for i in words:
    count+=1
print(count)