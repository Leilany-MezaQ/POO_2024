from clases import*
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
        return math.pi 

