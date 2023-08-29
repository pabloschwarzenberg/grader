import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def camino(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y

        if dx == 0 and dy == 0:
            print("Las ciudades son la misma.")
        else:
            pasos = []
            distancia_total = 0

            while dx != 0 or dy != 0:
                paso_x = 1 if dx > 0 else -1 if dx < 0 else 0
                paso_y = 1 if dy > 0 else -1 if dy < 0 else 0

                distancia = math.sqrt(paso_x**2 + paso_y**2)
                distancia_total += distancia

                pasos.append((paso_x, paso_y))
                dx -= paso_x
                dy -= paso_y

            print("Camino:")
            for paso in pasos:
                print(f"Moverse {paso[0]} en el eje x y {paso[1]} en el eje y.")

            print("Distancia total:", distancia_total)

    def distancia(self, otra_ciudad):
        dx = otra_ciudad.x - self.x
        dy = otra_ciudad.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

if __name__ == "__main__":
    p1 = Ciudad(1, 1)
    p2 = Ciudad(3, 3)
    p1.camino(p2)
