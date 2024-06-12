'''5.- Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION
imprimir la información'''

# Crear una lista con los valores de la tabla
accion = ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"]
terror = ["LA MONJA", "EL CONJURO", "LA MALDICION"]
deportes = ["ESPN", "MAS DEPORTE", "ACCION"]

# Crear un diccionario con las listas como claves y valores
tabla_dict = {
    "ACCION": accion,
    "TERROR": terror,
    "DEPORTES": deportes
}

# Imprimir la información del diccionario
for categoria, peliculas in tabla_dict.items():
    print(f"{categoria}: {', '.join(peliculas)}")
