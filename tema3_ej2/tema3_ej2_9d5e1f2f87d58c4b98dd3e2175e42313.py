class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("La operación de suma solo es válida entre objetos de la clase Vector3D.")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


def suma_vectores(v1, v2):
    if isinstance(v1, Vector3D) and isinstance(v2, Vector3D):
        return v1 + v2
    else:
        raise TypeError("La función suma_vectores solo acepta objetos de la clase Vector3D como parámetros.")


if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)
    c = suma_vectores(a, b)
    print("Vector a:", a)
    print("Vector b:", b)
    print("Vector c (suma de a y b):", c)
    print("Norma de c:", c.norma())
