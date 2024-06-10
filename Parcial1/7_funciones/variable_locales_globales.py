def calcular_area_rectangulo(base, altura):
    # Estas son variables locales
    area = base * altura
    mensaje = f"El área del rectángulo es {area} unidades cuadradas."
    return mensaje

def calcular_perimetro_rectangulo(base, altura):
    # Estas son variables locales
    perimetro = 2 * (base + altura)
    mensaje = f"El perímetro del rectángulo es {perimetro} unidades."
    return mensaje

# Definimos las dimensiones del rectángulo
base = 5
altura = 10

# Llamamos a las funciones y mostramos los resultados
resultado_area = calcular_area_rectangulo(base, altura)
resultado_perimetro = calcular_perimetro_rectangulo(base, altura)

print(resultado_area)
print(resultado_perimetro)

 
     
     
    