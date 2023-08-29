class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return ((self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5)

    def __add__(self, other):
        x_sum = self.x + other.x
        y_sum = self.y + other.y
        z_sum = self.z + other.z
        return Vector(x_sum, y_sum, z_sum)


def suma_vectores(v1, v2):
    return v1 + v2


if __name__ == "__main__":
    vector1 = Vector(1, 2, 3)
    vector2 = Vector(4, 5, 6)

    print(vector1.norma())  # 3.7416573867739413
    print(vector2.norma())  # 8.774964387392123

    vector_suma = suma_vectores(vector1, vector2)
    print(vector_suma.x, vector_suma.y, vector_suma.z)  # 5, 7, 9
