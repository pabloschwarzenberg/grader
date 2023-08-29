# crea la clase Vector y completa el código de la función suma_vectores usándola
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise ValueError("Operands must be instances of Vector")

def suma_vectores(v1, v2):
    if isinstance(v1, Vector) and isinstance(v2, Vector):
        x_sum = v1.x + v2.x
        y_sum = v1.y + v2.y
        z_sum = v1.z + v2.z
        return Vector(x_sum, y_sum, z_sum)
    else:
        raise ValueError("Operands must be instances of Vector")

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print(v1.norma())  # 3.7416573867739413
    print(v2.norma())  # 8.774964387392123

    v3 = v1 + v2
    print(v3.x, v3.y, v3.z)  # 5, 7, 9

    v4 = suma_vectores(v1, v2)
    print(v4.x, v4.y, v4.z)  # 5, 7, 9
