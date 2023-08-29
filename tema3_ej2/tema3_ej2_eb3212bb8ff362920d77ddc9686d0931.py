class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector3D):
            x = self.x + other.x
            y = self.y + other.y
            z = self.z + other.z
            return Vector3D(x, y, z)
        else:
            raise TypeError("Operación no válida. Se requiere un objeto de la clase Vector3D.")

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


def suma_vectores(v1, v2):
    return v1 + v2


if __name__ == "__main__":
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    print("La norma del vector v1 es:", v1.norma())
    print("La norma del vector v2 es:", v2.norma())
    v3 = suma_vectores(v1, v2)
    print("La suma de los vectores v1 y v2 es:", v3)
    v4 = v1 + v2
    print("La suma de los vectores v1 y v2 es:", v4)