# Solicitar dos números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Asegurarnos de que el primer número sea menor o igual al segundo
if numero1 <= numero2:
    # Mostrar los números en el rango (incluyendo ambos extremos)
    for num in range(numero1, numero2 + 1):
        print(num)
else:
    print("El primer número debe ser menor o igual al segundo.")
