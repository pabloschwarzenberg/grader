
class Ciudad:
    def __init__(self, posX, posY):
        self.posX = int(posX)
        self.posY = int(posY)
    def camino(self, other):
        pie_x = self.posX
        pie_y = self.posY
        dx = self.posX - other.posX
        dy = self.posY - other.posY
        pasos = [[self.posX, self.posY]]
        while pie_x != other.posX and pie_y != other.posY:
            pie_x += abs(-dx)/(-dx)
            pie_y += abs(-dy)/(-dy)
            pasos.append([pie_x, pie_y])
        if pie_x != other.posX:
            while pie_x != other.posX:
                pie_x += abs(-dx)/(-dx)
                pasos.append([pie_x,pie_y])
    
        elif pie_y != other.posY:
            while pie_y != other.posY:
                pie_y += abs(-dy)/(-dy)
                pasos.append([pie_x,pie_y])            
            

        return pasos            
      
    def distancia(self, other):
        dist = 0    
        rec = self.camino(other)
        try:
            for i in range(len(rec)):
            
                dx = rec[i][0] - rec[i+1][0]
                dy = rec[i][1] - rec[i+1][1]
                d = (dx * dx + dy * dy)**(1/2)
                dist += d
        except:
            pass
        return dist
  

if __name__ == "__main__":
    p1=Ciudad(1,1)
    p2=Ciudad(3,3)
    print(p1.camino(p2))
    print(p1.distancia(p2))