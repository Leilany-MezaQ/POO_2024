'''agenda=[
["carlos",6182936578],
["karin",6182936556],
["Lola",6182936556],
["Pedro",6182936534],
]
print(agenda)
for i in agenda:
 print(f"{agenda.index(i)+1}.-{i}")
 
 #ejemplo 5 crear un programa que permita gestionar (administrar peliculas),
 # colocar un menu de opciones para agregar, remover y consultar peliculas 
 #Nota utilizar funciones y mandar llamar desde otro archivo utilizar listas para almacenar los nombres de las peliculas'''
 
 
# Archivo principal (main.py)

# Importa el módulo donde tienes las funciones
import peliculas_funciones

# Lista para almacenar los nombres de las películas
peliculas = []

def mostrar_menu():
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Actualizar película")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre_pelicula = input("Ingresa el nombre de la película: ")
            peliculas_funciones.agregar_pelicula(peliculas, nombre_pelicula)
        elif opcion == "2":
            nombre_pelicula = input("Ingresa el nombre de la película a remover: ")
            peliculas_funciones.remover_pelicula(peliculas, nombre_pelicula)
        elif opcion == "3":
            peliculas_funciones.consultar_peliculas(peliculas)
        elif opcion == "4":
            nombre_pelicula = input("Ingresa el nombre de la película a actualizar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre de la película: ")
            peliculas_funciones.actualizar_pelicula(peliculas, nombre_pelicula, nuevo_nombre)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()