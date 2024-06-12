from peliculas import agregar_pelicula, remover_pelicula, consultar_peliculas, vaciar_peliculas, buscar_pelicula, actualizar_pelicula

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nGestión de Películas")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Vaciar lista de películas")
    print("5. Buscar película")
    print("6. Actualizar película")
    print("7. Salir")

def main():
    peliculas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la película: ")
            anio = input("Ingrese el año de lanzamiento: ")
            genero = input("Ingrese el género: ")
            agregar_pelicula(peliculas, nombre, anio, genero)
        elif opcion == '2':
            nombre = input("Ingrese el nombre de la película a remover: ")
            confirmar = input(f"¿Está seguro de que desea remover la película '{nombre}'? (s/n): ")
            if confirmar.lower() == 's':
                remover_pelicula(peliculas, nombre)
            else:
                print("Acción cancelada.")
        elif opcion == '3':
            consultar_peliculas(peliculas)
        elif opcion == '4':
            vaciar_peliculas(peliculas)
            print("Lista de películas vaciada.")
        elif opcion == '5':
            nombre = input("Ingrese el nombre de la película a buscar: ")
            buscar_pelicula(peliculas, nombre)
        elif opcion == '6':
            nombre = input("Ingrese el nombre de la película a actualizar: ")
            actualizar_pelicula(peliculas, nombre)
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
    
