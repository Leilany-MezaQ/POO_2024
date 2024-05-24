# El ciclo while es una estructura de control que itera o repite la ejecucíon de una serie de instrucciones tantas veces como la condicion se cumpla 'True'

# Sintaxi:

#  while condicion:
#     bloque instrucciones

#ejemplo 1 crear un programa que imprima 5 veces el caracter @

contador=1
while contador<=5:
    print("@")
    contador+=1

#Ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma 

contador=1
suma=0
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
print(f"La suma es: {suma}")    

#Ejemplo 3 crear un programa que solicite un numero entero e continuacion imprima la tabla de multiplicar correspondiente
numero=int(input("Ingresa un numero: "))

multi=0
i=1
while i<=10:
  multi=i*numero
  print(f"{numero} X {i} = {multi}")
  i+=1