'''2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for'''
 
 
 # Crear una lista vacía
mi_lista = []

# Usar un ciclo while para agregar valores hasta que la longitud sea menor a 120
while len(mi_lista) < 120:
    valor = int(input("Ingresa un valor (0 para finalizar): "))
    if valor == 0:
        break  # Salir del ciclo si se ingresa 0
    mi_lista.append(valor)

# Mostrar la lista
print("Lista completa:")
for elemento in mi_lista:
    print(elemento)
