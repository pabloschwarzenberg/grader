import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type: {} and {}".format(type(self), type(other)))

    def __repr__(self):
        return "Vector3D({}, {}, {})".format(self.x, self.y, self.z)


def suma_vectores(v1, v2):
    if isinstance(v1, Vector3D) and isinstance(v2, Vector3D):
        return v1 + v2
    else:
        raise TypeError("Unsupported operand types: {} and {}".format(type(v1), type(v2)))


def main():
    x1 = float(input("Ingrese la coordenada x del primer vector: "))
    y1 = float(input("Ingrese la coordenada y del primer vector: "))
    z1 = float(input("Ingrese la coordenada z del primer vector: "))

    v1 = Vector3D(x1, y1, z1)

    x2 = float(input("Ingrese la coordenada x del segundo vector: "))
    y2 = float(input("Ingrese la coordenada y del segundo vector: "))
    z2 = float(input("Ingrese la coordenada z del segundo vector: "))

    v2 = Vector3D(x2, y2, z2)

    print("Primer vector: {}".format(v1))
    print("Segundo vector: {}".format(v2))

    v3 = suma_vectores(v1, v2)
    print("Suma de vectores: {}".format(v3))
    print("Norma del vector resultante: {}".format(v3.norma()))


if __name__ == "__main__":
    main()

