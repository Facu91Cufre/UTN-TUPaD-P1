import random, timeit
continuar = True

# Ordenamiento burbuja
def burbuja(lista):
    # Se crea una copia de la lista para no afectar la original
    lista = lista.copy()
    # Se obtiene el largo de la lista
    largo_lista = len(lista)
    # Bucle externo que recorre toda la lista
    for i in range(largo_lista):
    # Bucle interno que comparará elementos adyacentes y los intercambia si están desordenados
        for j in range(0, largo_lista - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Quick Sort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        # Se elige el primer elemento como pivot
        pivot = lista[0]
        # Sublista con los elementos que sean menores o iguales al pivot
        menos = [x for x in lista[1:] if x <= pivot]
        # Sublista con los elementos que sean mayores al pivot
        mayor_que = [x for x in lista[1:] if x > pivot]
        # Se llama recursivamente a la función quicksort y se le concatenan los resultados
        return quicksort(menos) + [pivot] + quicksort(mayor_que)

# Búsqueda binaria:
def busqueda_binaria(lista, objetivo):
    # Se definen los extremos
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        # Se calcula el índice del elemento del medio
        medio = (izquierda + derecha) // 2
        # Si el elemento del medio es el objetivo, se retorna su índice
        if lista[medio] == objetivo:
            return medio
        # Si el objetivo es mayor, se descarta la mitad izquierda
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        # Si el objetivo es menor, se descarta la mitad derecha
        else:
            derecha = medio - 1
    return -1

# Búsqueda lineal:
def busqueda_lineal(lista, objetivo):
    # Se recorre la lista
    for i in range(len(lista)):
    # Si el elemento actual es igual al objetivo retorna el índice
        if lista[i] == objetivo:
            return i
    # Si no encuentra el objetivo retorna -1
    return -1

# Función para mostrar lista
def mostrar_lista(lista):
    if not lista:
        print("La lista está vacía.")
    else:
        print("Lista de apellidos: ")
        for apellido in lista:
            print(f"Apellido: {apellido}")
        print()

# Función para medir tiempo de búsqueda
def medir_tiempo_busqueda(algoritmo, lista, objetivo):
    inicio = timeit.default_timer()
    resultado = algoritmo(lista,objetivo)
    fin = timeit.default_timer()
    tamano = len(lista)
    tipo = "grande" if tamano > 500 else "pequeña"
    print(f"El método {algoritmo.__name__} encontró el elemento {objetivo} en la posición {resultado} y tardó para una lista {tipo}: {fin - inicio} segundos.")
    print()

# Función para medir el tiempo de ordenamiento
def medir_tiempo(algoritmo, lista):
    inicio = timeit.default_timer()
    algoritmo(lista)
    fin = timeit.default_timer()
    tamano = len(lista)
    tipo = "grande" if tamano > 500 else "pequeña"
    print(f"El método {algoritmo.__name__} tardó para una lista {tipo}: {fin - inicio} segundos.")
    print()

# Lista pequeña de apellidos
apellidos = [
    "González", "Rodríguez", "García", "Martínez", "López",
    "Pérez", "Sanchez", "Ramírez", "Torres", "Flores",
    "Rivera", "Gómez", "Díaz", "Cruz", "Morales",
    "Vargas", "Castillo", "Jiménez", "Ramos", "Ortiz",
    "Silva", "Romero", "Mendoza", "Herrera", "Alvarez",
    "Castro", "Ruiz", "Navarro", "Domínguez", "Campos",
    "Gutierrez", "Soto", "Delgado", "Mora", "Rojas",
    "Vega", "Acosta", "Salazar", "Valencia", "Pacheco",
    "Benítez", "Medina", "Figueroa", "Cabrera", "Rivas",
    "Marín", "Santana", "Peña", "Cortés", "Cufré"
]

# Generamos una lista grande con diez mil numeros sin repetirse para el caso de listas grandes
tamaño_lista_random = 10000
lista_random = random.sample(range(1, 1000000), tamaño_lista_random)
lista_random_ordenada = sorted(lista_random)

# Ordenar lista
lista_ordenada = burbuja(apellidos)
# Llamada a la función mostrar_lista
mostrar_lista(lista_ordenada)
# Llamada a la función medir tiempo para calcular cuanto tardan ambos algoritmos tanto con la lista pequeña como la grande.
medir_tiempo(burbuja, apellidos)
medir_tiempo(quicksort, apellidos)
medir_tiempo(burbuja, lista_random)
medir_tiempo(quicksort, lista_random)

# Menú para la búsqueda
while continuar:
    elemento_busqueda = lista_random[5000]
    opcion = int(input("Ingrese 1 para usar la búsqueda lineal, 2 para utilizar la búsqueda binaria o 0 para salir: "))
    if opcion == 0:
        continuar = False
    elif opcion in (1,2):
        elemento = input("Ingrese el elemento que quiere buscar: ")
        print()
        algoritmo = busqueda_lineal if opcion == 1 else busqueda_binaria
        posicion = algoritmo(lista_ordenada, elemento)
        medir_tiempo_busqueda(algoritmo, lista_ordenada, elemento)
        print(f"Ahora vamos a mostrar el tiempo que tarda {algoritmo.__name__} en una lista grande de números: ")
        medir_tiempo_busqueda(algoritmo, lista_random_ordenada, elemento_busqueda)
