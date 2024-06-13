# Este ciclo es un iterativo y se ejecura X veces de acuerdo a los valores numericos enteros establecidos

# sintaxis:
#  for variable in elemento_iterable(lista, rango, etc):
#     bloque de instrucciones

#ejemplo 1 crear un programa que imprima 5 veces el caracter @

for contador in range(1,6):
    print("@")

#Ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma 
suma=0
for numero in range(1,6):
  print(numero)
  suma+=numero
print(f"La suma es: {suma}")  

#Ejemplo 3 crear un programa que solicite un numero entero e continuacion imprima la tabla de multiplicar correspondiente
numero=int(input("Ingresa un numero: "))

multi=0
for i in range(1,11):
  multi=i*numero
  print(f"{numero} X {i} = {multi}")
  
  
  
  
  
  
  