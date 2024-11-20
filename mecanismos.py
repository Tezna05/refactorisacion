# Clase base para todas las formas geométricas
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Clase para el círculo
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

# Clase para el cuadrado
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Clase para el rectángulo
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Ejemplo de uso
shapes = [Circle(5), Square(4), Rectangle(3, 6)]

for shape in shapes:
    print(f"Area: {shape.area()}")
