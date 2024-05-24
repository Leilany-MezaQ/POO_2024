def calcular_porcentaje():
    numero = float(input("Introduce un número: "))
    porcentaje = float(input("Introduce el porcentaje (sin el símbolo %): "))

    resultado = (porcentaje / 100) * numero
    print(f"{porcentaje}% de {numero} es igual a {resultado}")

calcular_porcentaje()
