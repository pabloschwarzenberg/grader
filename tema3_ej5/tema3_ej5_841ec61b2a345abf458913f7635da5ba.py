import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        pasos = []
        distancia = max(abs(otra_ciudad.x - self.x), abs(otra_ciudad.y - self.y))
        
        for i in range(distancia + 1):
            x = self.x + i * (otra_ciudad.x - self.x) // distancia
            y = self.y + i * (otra_ciudad.y - self.y) // distancia
            pasos.append([x, y])
        
        return pasos
    
    def distancia(self, otra_ciudad):
        return math.sqrt((otra_ciudad.x - self.x)**2 + (otra_ciudad.y - self.y)**2)



if __name__ == "__main__":
  pass
         