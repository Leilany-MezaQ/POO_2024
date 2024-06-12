''' 4.-Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones'''
  
def imprimir_tipo(variable):
    if isinstance(variable, list):
        print(f"La variable es una lista: {variable}")
    elif isinstance(variable, str):
        print(f"La variable es una cadena: {variable}")
    elif isinstance(variable, int):
        print(f"La variable es un entero: {variable}")
    elif isinstance(variable, bool):
        print(f"La variable es un valor lógico: {variable}")
    else:
        print("Tipo de dato no reconocido")

# Crear las variables
mi_lista = [1, 2, 3]
mi_cadena = "Hola, mundo"
mi_entero = 42
mi_logico = True

# Imprimir mensajes según el tipo de dato
imprimir_tipo(mi_lista)
imprimir_tipo(mi_cadena)
imprimir_tipo(mi_entero)
imprimir_tipo(mi_logico)
