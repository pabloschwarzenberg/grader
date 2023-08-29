class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        return Vector(v1.x + v2.x, v1.y + v2.y, v1.z + v2.z)
    else:
        return None

if __name__ == "__main__":
    # Ejemplo de uso
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)
    print(a)
    print(b)
    print(suma_vectores(a, b))
    print(a+b)
    print(a.norma())
    print(b.norma())