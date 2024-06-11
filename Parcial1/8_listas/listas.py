"""
    List(Array)
    son colecciones o conjunto de datos/valores
    bajo un mismo nombre, para acceder a los
    valores se hace con un indice numerico

    Nota: sus valores si son modificables

    La lista es una colección ordenada y 
    modificable. Permite miembros duplicados.

"""
import os
os.system("cls")

#ejemplo 1: Crear una lista e imprimir el contenido
# lista = [23,34]
# print(lista)

# #Recorrer la lista con el for
# for i in lista:
#     print(i)

#Recorrer la lista con while
# i=0
# while i <= len(lista)-1:
#     print(lista[i])
#     i+=1

#ejemplo 2: crear una lista con palabras, solicitar una palabra
#y buscar la coincidencia en la lista e indicar si la encontró o no y su posición

# lis=["hola","dos","vallejin","popo"]
# buscarPal=input("Ingresa la palabra a buscar: ")

# nofind=True
# for i in lis:
#     if buscarPal == i:
#         print(f"Si está la palabra {i}. Está en la posición {lis.index(i)}")
#         nofind=True

# if nofind:
#     print("No está la palabra")

# i=0
# while i <= len(lis)-1:
#     if buscarPal == lis[i]:
#         print(f"La palabra {buscarPal} esta en la posición {i}")
#         nofind=False
#     i+=1

# if nofind:
#     print("No está la palabra")

os.system("cls")

# #ejemplo 3: Agregar y eliminar elementos de una lista
# numeros=[2,3]
# print(numeros)

# #agrgar un elemento

# #append solo inserta en la siguiente posicion el elemento dado
# numeros.append(100)
# #insert es en el lugar especifico y el elemento a agregar
# numeros.insert(1,100)

# print(numeros)

# #eliminar un elemento

# #remove es para eliminar el elemento puesto
# numeros.remove(100)
# print(numeros)

# #pop es para elegir el elemento segun su posicion
# numeros.pop(2)
# print(numeros)

#Ejemplo 4 Crear una lista multidimensional (matriz) para
#almacenar contactos telefonicos

# agenda = [
#     ["Karin",6181234567],
#     ["Leon",6182334556],
#     ["Pedro",6188989762]
# ]

# for i in agenda:
#     print(f"{agenda.index(i)+1}. {i}")

"""
ejemplo 5 Crear un programa que permita gestionar (administrar)
peliculas colocar un menu de opciones para agregar, remover,
consultar peliculas
Notas:
1. utilizar funciones y mandar llamar desde otro archivo
2. utilizar listas para almacenar nombres de peliculas

"""

from FuncionPeliculas import *
# peliculas = []
# def esperaTecla():
#     #Muestra mensaje
#     print("Presiona una tecla para continuar")
#     #Espera a que el usuario presione una tecla
#     input()

# def buscar():
#     print("Las películas registradas son: \n")
#     for i in peliculas:
#         print(f"{peliculas.index(i)+1}.- {i}\n")

# def Agregar():
#     pelicula = input("Ingese la película: ")
#     peliculas.append(pelicula)
#     print("\n Película agregada con éxito \n")

# def eliminar():
#     nofind=True
#     buscarPel = input("Ingrese la película a borrar: ")
#     for i in peliculas:
#         if buscarPel == i:
#             peliculas.pop(peliculas.index(i))
#             print("Se eliminó con éxito la película \n")
#             nofind=False
    
#     if nofind:
#         print("No está la película")


opcion= 1
while opcion != 4:
    os.system("cls")
    print("\n..::: Almacen de pelicuklas :::... \n 1.- Consultar \n 2.- Agregar \n 3.- Eliminar \n 4.- SALIR")
    opcion = input("Elige una opción: ").lower()

    if opcion == "1":
        buscar()
        esperaTecla()
    elif opcion == "2":
        Agregar()
        esperaTecla()
    elif opcion == "3":
        eliminar()
        esperaTecla()
    elif opcion == "4":
        print("Hasta luego :D")
        break
    else:
        print("La opción no es válida. Pruebe con otra.")
        esperaTecla()