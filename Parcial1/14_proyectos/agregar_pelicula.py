# peliculas.py

def agregar_pelicula(peliculas, nombre, anio, genero):
        pelicula = {'nombre': nombre, 'anio': anio, 'genero': genero}
        peliculas.append(pelicula)
        print(f'\033[92mPelícula "{nombre}" agregada.\033[0m')

def remover_pelicula(peliculas, nombre):
        for pelicula in peliculas:
            if pelicula['nombre'].lower() == nombre.lower():
                peliculas.remove(pelicula)
                print(f'\033[91mPelícula "{nombre}" removida.\033[0m')
                return
        print(f'\033[93mPelícula "{nombre}" no encontrada.\033[0m')

def consultar_peliculas(peliculas):
        if peliculas:
            print("\033[94mLista de películas:\033[0m")
            for pelicula in peliculas:
                print(f'\033[94m- {pelicula["nombre"]} ({pelicula["anio"]}, {pelicula["genero"]})\033[0m')
        else:
            print("\033[93mNo hay películas en la lista.\033[0m")