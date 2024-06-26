from clases import Rectangulo, Circulo

def main():
    # Crear un rectángulo
    rectangulo1 = Rectangulo(3, 4, True, 10, 20)
    print(f"Área del rectángulo: {rectangulo1.calcularArea()}")
    print(f"¿El rectángulo está visible? {'Sí' if rectangulo1.estaVisible() else 'No'}")
    
    rectangulo1.ocultar()
    print(f"¿El rectángulo está visible después de ocultar? {'Sí' if rectangulo1.estaVisible() else 'No'}")
    
    rectangulo1.mover(10, 15)
    print(f"El rectángulo se movió a la posición ({rectangulo1.x}, {rectangulo1.y})")

    # Crear un círculo
    circulo1 = Circulo(3, 3, True, 6)
    print(f"Área del círculo: {circulo1.calcularArea()}")
    print(f"¿El círculo está visible? {'Sí' if circulo1.estaVisible() else 'No'}")
    
    circulo1.ocultar()
    print(f"¿El círculo está visible después de ocultar? {'Sí' if circulo1.estaVisible() else 'No'}")
    
    circulo1.mover(8, 9)
    print(f"El círculo se movió a la posición ({circulo1.x}, {circulo1.y})")

if __name__ == "__main__":
    main()
