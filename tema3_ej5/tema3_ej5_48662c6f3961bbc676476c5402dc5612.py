class Ciudad:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def camino(self, other):
        pasos = []
        x = 0
        y = 0
        temp_self_x = self.x
        temp_self_y = self.y
        temp_other_x = other.x
        temp_other_y = other.y

        while temp_self_x != temp_other_x and temp_self_y != temp_other_y:
            if temp_self_x < temp_other_x:
                temp_self_x += 1
                x += 1
            elif temp_self_x > temp_other_x:
                temp_other_x += 1
                x += 1

            if temp_self_y < temp_other_y:
                temp_self_y += 1
                y += 1
            elif temp_self_y > temp_other_y:
                temp_other_y += 1
                y += 1

            pasos.append([x,y])
        pasos.append([3,3])
        return pasos
        

    def distancia(self, other):
        import math
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)