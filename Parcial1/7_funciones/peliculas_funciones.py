# Archivo peliculas_funciones.py

def agregar_pelicula(lista_peliculas, nombre_pelicula):
    lista_peliculas.append(nombre_pelicula)
    print(f"Película '{nombre_pelicula}' agregada correctamente.")

def remover_pelicula(lista_peliculas, nombre_pelicula):
    if nombre_pelicula in lista_peliculas:
        lista_peliculas.remove(nombre_pelicula)
        print(f"Película '{nombre_pelicula}' removida correctamente.")
    else:
        print(f"Película '{nombre_pelicula}' no encontrada.")

def consultar_peliculas(lista_peliculas):
    if lista_peliculas:
        print("Películas disponibles:")
        for pelicula in lista_peliculas:
            print(f"- {pelicula}")
    else:
        print("No hay películas registradas.")

def actualizar_pelicula(lista_peliculas, nombre_pelicula, nuevo_nombre):
    if nombre_pelicula in lista_peliculas:
        indice = lista_peliculas.index(nombre_pelicula)
        lista_peliculas[indice] = nuevo_nombre
        print(f"Película actualizada: '{nombre_pelicula}' -> '{nuevo_nombre}'.")
    else:
        print(f"Película '{nombre_pelicula}' no encontrada.")



