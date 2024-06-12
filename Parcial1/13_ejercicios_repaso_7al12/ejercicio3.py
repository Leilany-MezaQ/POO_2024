'''3.-Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas'''

def main():
    # Crear una lista vacía
    mi_lista = []

    # Llenar la lista con palabras o frases hasta que el usuario lo desee
    while True:
        palabra = input("Ingresa una palabra o frase (o presiona Enter para terminar): ")
        if not palabra:
            break
        mi_lista.append(palabra)

    # Imprimir el contenido de la lista en mayúsculas
    for elemento in mi_lista:
        print(elemento.upper())

if __name__ == "__main__":
    main()
