# 2.- Calculadora: escribir un programa que tome dos números como entrada y realice operaciones básicas como suma, resta y multiplicación y división.
num1 = input(print("Ingresa un número"))
num2 = input(print("Ingresa un segundo número"))

sum = int(num1) + int(num2)
print("Esta es una suma: " , sum)

res = num1-num2
print("Esta es una resta: " , res)

multi = num1 * num2
print("Esta es una multiplicación: " , multi)

div = num1 / num2
print("Esta es una división: " , div)
