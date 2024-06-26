from figuras import figuras, abstractmethod
import math

# Clase abstracta Figura
class Figura(figuras):
    
    @abstractmethod
    def calcular_area(self):
        pass

# Clase Rectángulo
class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho
        
    @property
    def largo(self):
        return self._largo
    
    @largo.setter
    def largo(self, valor):
        self._largo = valor
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor
    
    def calcular_area(self):
        return self._largo * self._ancho

# Clase Círculo
class Circulo(Figura):
    def __init__(self, radio):
        self._radio = radio
        
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, valor):
        self._radio = valor
    
    def calcular_area(self):
        return math.pi * (self._radio ** 2)

# Clase Triángulo
class Triangulo(Figura):
    def __init__(self, altura, ancho):
        self._altura = altura
        self._ancho = ancho
        
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        self._altura = valor
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor
    
    def calcular_area(self):
        return (self._altura * self._ancho) / 2

# Ejemplo de uso
rectangulo = Rectangulo(10, 5)
circulo = Circulo(7)
triangulo = Triangulo(8, 6)

print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Área del triángulo: {triangulo.calcular_area()}")
