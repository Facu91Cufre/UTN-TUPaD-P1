import random
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
for i in range(101):
    print(i)
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
num = input("Por favor ingrese un número: ")
digitos = len(num)
print(f"Su número tiene {digitos} dígitos.")
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
total = 0
numero_1 = int(input("Por favor ingrese el primer número: "))
numero_2 = int(input("Por favor ingrese el segundo número: "))
for i in range(numero_1 + 1, numero_2):
    total += i
print(total)
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 
total = 0
numero = int(input("Por favor ingrese un número: "))
while numero != 0:
    total += numero
    numero = int(input("Ingrese otro número: "))
print(f"El total acumulado es {total}.")
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
cont = 1
random_number = random.randint(0,9)
print(random_number)
usuario = int(input("Tratá de adivinar que número del 0 al 9 es el elegido: "))
while random_number != usuario:
    cont += 1
    usuario = int(input("Incorrecto. Ingresá otro número: "))
if random_number == usuario:
    print(f"Correcto! Lo adivinaste en {cont} intentos.")    
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente. 
for i in range(99,0,-1):
    if i % 2 == 0:
        print(i)
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 
total = 0
tope = int(input("Por favor ingrese un número entero positivo: "))
while tope <= 0:
    tope = int(input("El número ingresado debe ser un entero positivo: "))
for i in range(1,tope):
    total += i
print(total)
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
pos = 0
neg = 0
par = 0
impar = 0
for i in range(0, 10):
    numero = int(input("Por favor ingrese un número: "))
    if numero > 0:
        pos += 1
    else:
        neg += 1    
    if numero % 2 == 0:
        par += 1
    else:
        impar +=1
print(f"Ingresaste: {pos} números positivos, {neg} números negativos, {par} números pares y {impar} números impares.")
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor). 
total = 0
for i in range(0,100):
    numero = int(input("Por favor ingresa un número: "))
    total += numero
media = total / 100
print(f"La media de los números ingresados es: {media}")    
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Por favor ingrese un número: "))
string = str(numero)
reversed = string[::-1]
print(f"El número ingresado invertido es: {reversed}")