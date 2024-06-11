paises=["Mexico","USA","Brasil","Japon"]
numeros=[23,34,12.56,0.100]
texto=["Hola", True,23,3.141516]

#ordenar una lista
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort
print(numeros)


#Añadir elementos 
print(texto)
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto),True)
print(texto)

#inserta un dato o valor al final de la lista
texto.append(False)
print(texto)

#Eliminar elementos de la lista 
print(numeros)
numeros.remove(23)
print(numeros)
numeros.pop(0)
print(numeros)

#dar la vuelta a una lista
print(numeros)
numeros.reverse
print(numeros)

#buscar un dato dentro de una ista 
respuesta="Brasil" in paises
print(respuesta)

#cuantas veces aparece un valor dentro de una lista 
print(numeros)
numeros.append(23)
cuantos=numeros.count(23)
print(f"el numero 23 se encontro: {cuantos}")

#Unir listas 
print(paises)
paises.extend(numeros)
print(paises)
