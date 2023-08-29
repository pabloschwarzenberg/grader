# crea la clase Vector y completa el código de la función suma_vectores usándola
def suma_vectores(v1,v2):
  return

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


def suma_vectores(v1, v2):
    return v1 + v2


if __name__ == "__main__":
    a = Vector(1, 2, 3)
    b = Vector(4, 5, 6)

    c = suma_vectores(a, b)
    print(c.x, c.y, c.z)  # Output: 5, 7, 9

    d = a + b
    print(d.x, d.y, d.z)  # Output: 5, 7, 9

    norma_a = a.norma()
    norma_b = b.norma()
    print(norma_a)  # Output: 3.7416573867739413
    print(norma_b)  # Output: 8.774964387392123           