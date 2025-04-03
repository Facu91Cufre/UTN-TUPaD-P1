# Trabajo Práctico 3: Estructuras Condicionales

from statistics import mode, median, mean 

# Ejercicio 1
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# edad = int(input("Por favor ingrese su edad: "))
# if edad > 18:
#     print("Es mayor de edad.")

# Ejercicio 2
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# nota = int(input("Por favor ingrese su nota: "))
# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# Ejercicio 3
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = int(input("Por favor ingrese un número: "))
# if numero % 2 == 0:
#     print("Ha ingresado un número par.")
# else:
#     print("Por favor, ingrese un número par.")

# Ejercicio 4
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años. "

# edad = int(input("Por favor ingrese su edad: "))
# if edad < 12:
#     print("Niño")
# elif edad >= 12 and edad < 18:
#     print("Adolescente")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven")
# else:
#     print("Adulto")

# Ejercicio 5
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

# contrasena = input("Por favor ingrese la contraseña: ")
# length = len(contrasena)
# if length >= 8 and length <= 14:
#     print("Ha ingresado una contraseña correcta.")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Ejercicio 6
# Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)
# if media == mediana and mediana == moda:
#     print("No hay sesgo.")
# else:
#     if media > mediana and mediana > moda:
#         print("Hay sesgo positivo.")
#     elif media < mediana and mediana < moda:
#         print("Hay sesgo negativo.")

# Ejercicio 7
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

# Ejercicio 8
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Por favor ingrese su nombre: ")
# opcion = int(input("Ahora ingrese la opción 1, 2 o 3: "))

# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# else:
#     print(nombre.title())

# Ejercicio 9
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

# magnitud = float(input("Por favor ingrese la magnitud del terremoto: "))
# if magnitud >= 7:
#     print("Extremo (puede causar daños a gran escala).")
# else:
#     if magnitud >= 6:
#         print("Muy fuerte (puede causar daños significativos).")
#     elif magnitud >= 5:
#         print("Fuerte (puede causar daño en estructuras débiles).")
#     elif magnitud >= 4:
#         print("Moderado (sentido por personas, pero generalmente no causa daño).")
#     elif magnitud >= 3:
#         print("Leve (ligeramente perceptible).")
#     else:
#         print("Muy leve (imperceptible).")

# Ejercicio 10

hemisferio = input("¿En qué hemisferio se encuentra?").lower()
mes = input("¿Qué mes del año es?").lower()
dia = int(input("¿Qué dia es?"))

if (mes == "diciembre" and dia >= 21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia < 21):
    estacion = "Verano" if hemisferio == "sur" else "Invierno"
elif mes == "marzo" and dia >= 21 or mes == "abril" or mes == "mayo" or (mes == "junio" and dia < 21):
    estacion = "Otoño" if hemisferio == "sur" else "Primavera"
elif (mes == "junio" and dia >= 21) or mes == "julio" or mes == "agosto" or (mes == "septiembre" and dia < 21):
    estacion = "Invierno" if hemisferio == "sur" else "Verano"
elif (mes == "septiembre" and dia >= 21) or mes == "octubre " or mes == "noviembre" or (mes == "diciembre" and dia < 21):
    estacion = "Primavera" if hemisferio == "sur" else "Otoño"
print(f"Usted se encuentra en {estacion}.")    


