'''import os
import math
from varias_funciones import

def solicitarDatos():
    global n1, n2
    n1 = float(input("Número #1: "))
    n2 = float(input("Número #2: "))

def getCalculadora(num1, num2, operacion):
    if operacion in ("1", "+", "SUMA"):
        return f"{num1} + {num2} = {num1 + num2}"
    elif operacion in ("2", "-", "RESTA"):
        return f"{num1} - {num2} = {num1 - num2}"
    elif operacion in ("3", "*", "MULTIPLICACION"):
        return f"{num1} * {num2} = {num1 * num2}"
    elif operacion in ("4", "/", "DIVISION"):
        if num2 != 0:
            return f"{num1} / {num2} = {num1 / num2}"
        else:
            return "No se puede dividir entre cero."
    elif operacion in ("5", "^", "POTENCIA"):
        return f"{num1} ^ {num2} = {num1 ** num2}"
    elif operacion in ("6", "RAIZ", "RAIZ CUADRADA"):
        if num1 >= 0:
            return f"Raíz cuadrada de {num1} = {math.sqrt(num1)}"
        else:
            return "No se puede calcular la raíz cuadrada de un número negativo."
    else:
        return "Opción inválida. Por favor, vuelve a intentarlo."

def esperaTecla():
    # Muestra un mensaje
    print("Presiona cualquier tecla para continuar...")

    # Espera a que el usuario presione una tecla
    input()

opcion = True
while opcion:
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::...\n1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n5.- Potencia\n6.- Raíz Cuadrada\n7.- SALIR")
    opcion = input("\tElige una opción: ").upper()

    if opcion != "7":
        solicitarDatos()
        print(getCalculadora(n1, n2, opcion))
        esperaTecla()
    else:
        opcion = False
        print("Gracias por utilizar el sistema ...")'''

      
      
      