'''1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado'''
 
# Crear una lista con 8 números enteros
numeros = [10, 5, 8, 3, 15, 7, 12, 20]

# a. Recorrer y mostrar la lista
print("Lista de números:")
for numero in numeros:
    print(numero)

# b. Función para convertir la lista en un string
def lista_a_string(lista):
    return ', '.join(str(num) for num in lista)

resultado = lista_a_string(numeros)
print(f"La lista como string: {resultado}")

# c. Ordenar la lista y mostrarla
numeros.sort()
print("Lista ordenada:")
for numero in numeros:
    print(numero)

# d. Mostrar la longitud de la lista
longitud = len(numeros)
print(f"La longitud de la lista es: {longitud}")

# e. Buscar un número ingresado por el usuario
buscar_numero = int(input("Introduce un número para buscar en la lista: "))
if buscar_numero in numeros:
    print(f"{buscar_numero} está en la lista.")
else:
    print(f"{buscar_numero} no está en la lista.")

 