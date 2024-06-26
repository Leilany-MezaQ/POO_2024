class Figura:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def estaVisible(self):
        return self.visible

    def ocultar(self):
        self.visible = False

    def mostrar(self):
        self.visible = True

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcularArea(self):
        pass  # Método abstracto


class Rectangulo(Figura):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho

    def calcularArea(self):
        return self.alto * self.ancho

    def ocultar(self):
        super().ocultar()

    def mostrar(self):
        super().mostrar()

    def mover(self, x, y):
        super().mover(x, y)


class Circulo(Figura):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.radio = radio

    def calcularArea(self):
        import math
        return math.pi * (self.radio ** 2)

    def ocultar(self):
        super().ocultar()

    def mostrar(self):
        super().mostrar()

    def mover(self, x, y):
        super().mover(x, y)
