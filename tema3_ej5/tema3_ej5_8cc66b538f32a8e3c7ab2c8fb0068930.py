import math

class Ciudad:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def camino(self, other):
        pasos=[]
        punto=[]
        x1=self.x
        x2=other.x
        y1=self.y
        y2=other.y

        punto=[x1,y1]
        pasos.append(punto)
        
        while x1!=x2 or y1!=y2:
            if x1<x2:
                x1=x1+1
            elif x1>x2:
                x1=x1-1

            if y1<y2:
                y1=y1+1
            elif y1>y2:
                y1=y1-1

            punto=[x1,y1]
            pasos.append(punto)

        punto=[x2,y2]
        pasos.append(punto)

        return pasos
        
    def distancia(self, other):
        x1=self.x
        x2=other.x
        y1=self.y
        y2=other.y

        x3=x2-x1
        y3=y2-y1

        z=x3*x3 + y3*y3

        distance=math.sqrt(z)
        return distance

if __name__ == "__main__":
    x1=int(input("Ciudad 1 x: "))
    y1=int(input("Ciudad 1 y: "))
    x2=int(input("Ciudad 2 x: "))
    y2=int(input("Ciudad 2 y: "))

    p1=Ciudad(x1,y1)
    p2=Ciudad(x2,y2)