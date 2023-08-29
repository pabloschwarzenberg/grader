class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def norma(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def __add__(self, other):
        if isinstance(other, Vector):
            x_sum = self.x + other.x
            y_sum = self.y + other.y
            z_sum = self.z + other.z
            return Vector(x_sum, y_sum, z_sum)
        else:
            raise TypeError("La suma solo es válida para objetos de la clase Vector")
        if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print(f"Norma de v1: {v1.norma()}")
    
    suma = v1 + v2
    print(f"Suma de v1 y v2: ({suma.x}, {suma.y}, {suma.z})")

         