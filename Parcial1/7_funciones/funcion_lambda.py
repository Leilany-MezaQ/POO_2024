 # Definimos una función lambda para mezclar ingredientes
mezclar_ingredientes = lambda ing1, ing2: f'Mezclando {ing1} con {ing2}'

# Utilizamos la función lambda para mezclar ingredientes
resultado = mezclar_ingredientes("harina", "azúcar")

# Imprimimos el resultado
print(resultado)  # Esto imprimirá "Mezclando harina con azúcar"
[10:08 p.m., 10/6/2024] Ángel De Jisus: # Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usamos una función lambda para filtrar los números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Imprimimos el resultado
print(numeros_pares)  # Esto imprimirá [2, 4, 6, 8, 10]
