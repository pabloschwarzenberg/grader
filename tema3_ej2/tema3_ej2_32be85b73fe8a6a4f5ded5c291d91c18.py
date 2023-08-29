class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


def suma_vectores(v1, v2):
    return v1 + v2


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    v3 = suma_vectores(v1, v2)
    print(v3.x, v3.y, v3.z)  # 5 7 9

    norma_v1 = v1.norma()
    print(norma_v1)  # 3.7416573867739413