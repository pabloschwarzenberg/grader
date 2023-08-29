class Ciudad:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distancia(self,other):
        return abs(((self.x-other.x)**2 + (self.y-other.y)**2)**(1/2))

    def camino(self,other):
        trayectoria = []
        paso = [self.x,self.y]
        while paso[0] != other.x or paso[1] != other.y:
            x = paso[0]
            y = paso[1]
            trayectoria.append([x, y])
            if paso[0] > other.x:
                paso[0] += -1
            else:
                paso[0] += 1

            if paso[1] > other.y:
                paso[1] += -1
            else:
                paso[1] += 1

        trayectoria.append(paso)
        return trayectoria

if __name__ == "__main__":
    pass