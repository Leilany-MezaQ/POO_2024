def mostrar_cuadrados_while(n):
    a = 1
    while a <= n:
        print(a ** 2)
        a += 1

# Mostrar los cuadrados de los primeros 60 números naturales
mostrar_cuadrados_while(60)

def mostrar_cuadrados_for(n):
    for a in range(1, n + 1):
        print(a ** 2)

# Mostrar los cuadrados de los primeros 60 números naturales
mostrar_cuadrados_for(60)