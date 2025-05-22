import math

#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

mensaje = saludar_usuario(input("Por favor ingrese su nombre: "))
print(mensaje)

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = int(input("Por favor ingrese su edad: "))
residencia = input("Por favor ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Por favor ingrese el radio del círculo: "))
print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Por favor ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print(f"Los segundos ingresados son {horas} horas.")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Por favor ingrese un número: "))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

resultados = operaciones_basicas(7,5)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Por favor ingrese su peso: "))
altura = float(input("Por favor ingrese su altura: "))

IMC = calcular_imc(peso, altura)
print(f"Su IMC es {IMC:.2f}.")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(temperatura):
    return (temperatura * 9/5) + 32

celsius = float(input("Por favor ingrese la temperatura en Celsius: "))
resultado = celsius_a_fahrenheit(celsius)
print(f"La temperatura ingresada en Fahrenheit es: {resultado}°F.")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a,b,c):
    return (a + b + c) / 3

nota1 = float(input("Por favor ingrese la Nota N°1: "))
nota2 = float(input("Por favor ingrese la Nota N°2: "))
nota3 = float(input("Por favor ingrese la Nota N°3: "))
promedio = calcular_promedio(nota1, nota2, nota3)

print(f"El promedio de las notas ingresadas es: {promedio:.2f}.")