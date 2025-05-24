#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario. 

def validar_numero(mensaje, min = float("-inf"), max = float("inf")):
    n = int(input(f"{mensaje}"))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}"))
    return n

def calcular_factorial(num):
    if num  == 0:
        return 1
    else:
        return num * calcular_factorial(num - 1)

def output_factorial(num):
    for i in range(1, num + 1):
        print(f"El factorial de {i} es: {calcular_factorial(i)}")

numero_validado = validar_numero("Por favor ingrese un número entero positivo: ", 1)
output_factorial(numero_validado)

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

valor_usuario = validar_numero("Por favor ingrese la posición que quiere de la serie Fibonacci: ", 1)

def posicion_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return posicion_fib(num - 1) + posicion_fib(num - 2)

def mostrar_serie_completa(num):
    serie = []
    for i in range(num):
        serie.append(posicion_fib(i))
    return serie

print(f"En la posición {valor_usuario} el valor es: {posicion_fib(valor_usuario - 1)}")
print(f"La serie completa es: {mostrar_serie_completa(valor_usuario)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general. 

def calcular_potencia(num, exponente):
    return 1 if exponente == 0 else num * calcular_potencia(num, exponente - 1)

def mostrar_potencia(numero, exponente):
    print(f"{numero} elevado a la {exponente} es: {calcular_potencia(numero, exponente)}")

n = int(input("Por favor ingrese un número: "))
e = int(input("Ahora ingrese el exponente: "))

mostrar_potencia(n, e)

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num//2) + str(num % 2)

print(decimal_a_binario(45))

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

def es_palindromo(palabra):
    if palabra == "":
        return True
    elif palabra[1:-1] == "":
        return True
    else:
        return es_palindromo(palabra[1:-1]) if palabra[0] == palabra[-1] else False

def confirmar_palindromo(palabra):
    palabra = palabra.capitalize()
    return f"{palabra} es un palíndromo." if es_palindromo(palabra) else f"{palabra} no es un palíndromo." 
   
palabra_usuario = input("Por favor ingrese una palabra: ")

print(confirmar_palindromo(palabra_usuario))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + suma_digitos(numero//10)
    
print(suma_digitos(431))

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    
print(contar_bloques(4))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número. 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if digito == numero%10 else 0) + contar_digito(numero//10, digito)

print(contar_digito(4387464, 4))
