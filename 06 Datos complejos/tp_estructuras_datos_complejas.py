# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
# # Añadir las siguientes frutas con sus respectivos precios: 
# # ● Naranja = 1200 
# # ● Manzana = 1500 
# # ● Pera = 2300 
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

# # 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# # ● Banana = 1330 
# # ● Manzana = 1700 
# # ● Melón = 2800
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

# # 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas = precios_frutas.keys()
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

numeros_telefonicos = {}
for i in range(5):
    clave = input(f"Por favor ingrese nombre del contacto N°{i + 1}: ")
    valor = input("Ahora ingrese el número de teléfono: ")
    numeros_telefonicos[f"{clave}"] = valor
print(numeros_telefonicos)
nombre = input("Ingrese el nombre de un contacto: ")
print(numeros_telefonicos[f"{nombre}"])

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Por favor ingrese una frase: ")
lista = frase.split()
palabras_unicas = set(lista)
print(palabras_unicas)

contador_de_palabras = {}
for palabra in lista:
    contador_de_palabras[palabra] = contador_de_palabras.get(palabra, 0) + 1

print(contador_de_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}
for x in range(3):
    alumno = input("Ingrese el nombre del alumno: ")
    notas = []
    for y in range(3):
        nota = float(input(f"Ingrese la nota N°{y + 1}: "))
        notas.append(nota)
    
    alumnos[alumno] = tuple(notas)
print(alumnos)

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = ["Martina","Sofía","Lucas","Valentina","Matías","Camila","Tomás","Agustina","Florencia"]
parcial_2 = ["Martina","Lucas","Valentina","Matías","Tomás","Agustina","Florencia"]

def obtener_aprobados(primer_parcial, segundo_parcial):
    alumnos_aprobados = {}
    for alumno in primer_parcial:
        alumnos_aprobados[alumno] = alumnos_aprobados.get(alumno, 0) + 1
    for alumno in segundo_parcial:
        alumnos_aprobados[alumno] = alumnos_aprobados.get(alumno, 0) + 1
    return alumnos_aprobados

def parciales_aprobados(diccionario):
    aprobaron_ambos_parciales = []
    aprobaron_un_parcial = []
    for alumno in diccionario:
        if diccionario[alumno] == 2:
            aprobaron_ambos_parciales.append(alumno)
        else:
            aprobaron_un_parcial.append(alumno)
    return aprobaron_ambos_parciales, aprobaron_un_parcial

def set_alumnos_aprobados(mensaje, lista):
    sin_repetir = set(lista)
    return f"{mensaje}: {sin_repetir}"
    
todos_los_aprobados = parcial_1 + parcial_2
aprobados = obtener_aprobados(parcial_1, parcial_2)
ambos_parciales, solo_uno = parciales_aprobados(aprobados)
resultado_set = set_alumnos_aprobados("Los que aprobaron al menos un parcial son: ", todos_los_aprobados)
print(f"Aprobaron ambos parciales: {ambos_parciales}. Aprobaron un parcial: {solo_uno}")
print(resultado_set)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe.

stock = {}
continuar = True

def agregar_stock(mensaje):
    producto = input(mensaje)
    while producto != "":
        if producto in stock:
            stock[producto] += 1
        else:
            stock[producto] = 1
        producto = input(mensaje)

def mostrar_stock(mensaje):
    producto = input(mensaje)
    cantidad = stock.get(producto)
    print(cantidad)
    return f"{producto}: {cantidad}" if cantidad else "El producto no está en stock."

def mostrar_todo_stock():
    if not stock:
        print("El stock está vacío.")
    else:
        print("Stock completo:")
        for producto, cantidad in stock.items():
            print(f"{producto}: {cantidad}")

while continuar:
    usuario = int(input("Por favor ingrese 1 para agregar un producto, 2 para revisar stock del producto, 3 para ver el stock completo o 0 para salir: "))
    if usuario == 1:
        agregar_stock("Por favor ingrese el nombre del producto o deje en blanco para salir: ", )
    elif usuario == 2:
        print(mostrar_stock("Ingrese el nombre del producto: "))
    elif usuario == 3:
        mostrar_todo_stock()
    else:
        continuar = False

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda = {
    ("lunes", "19:00"): "Clase Organización Empresarial",
    ("martes", "18:00"): "Clase Matemáticas",
    ("martes", "19:00"): "Clase Arquitectura y Sistemas Operativos",
    ("martes", "20:00"): "Clase Organización Programación I",
    ("Miercoles", "19:00"): "Clase Organización Empresarial",
    ("Jueves", "18:00"): "Clase Matemáticas",
    ("Jueves", "19:00"): "Clase Arquitectura y Sistemas Operativos",
    ("Jueves", "20:00"): "Clase Organización Programación I"
}

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores.

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Estados Unidos": "Washington D.C.",
    "Canadá": "Ottawa",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}

def cambiar_par_clave_valor(diccionario):
    nuevo_diccionario = {}
    for clave, valor in diccionario.items():
        nuevo_diccionario[valor] = clave
    return nuevo_diccionario
print(cambiar_par_clave_valor(paises))