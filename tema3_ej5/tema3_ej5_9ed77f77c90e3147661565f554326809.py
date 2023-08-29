import math

class Ciudad:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def camino(self, otra_ciudad):
        pasos = []
        curr_x = self.x
        curr_y = self.y
        
        while curr_x != otra_ciudad.x or curr_y != otra_ciudad.y:
            pasos.append([curr_x, curr_y])
            
            if curr_x < otra_ciudad.x:
                curr_x += 1
            elif curr_x > otra_ciudad.x:
                curr_x -= 1
            
            if curr_y < otra_ciudad.y:
                curr_y += 1
            elif curr_y > otra_ciudad.y:
                curr_y -= 1
        
        pasos.append([curr_x, curr_y])
        
        return pasos
    
    def distancia(self, otra_ciudad):
        distancia_x = otra_ciudad.x - self.x
        distancia_y = otra_ciudad.y - self.y
        distancia = math.sqrt(distancia_x ** 2 + distancia_y ** 2)
        return (distancia)
