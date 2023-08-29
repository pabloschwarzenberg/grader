import math
class Ciudad:
    def __init__(self,x,y):
        self.punto=[]
        self.punto.append(x)
        self.punto.append(y)
    def camino(self,other):
        a=self.punto.copy()
        b=[]
        while a!=other.punto:
            b.append(list(a))
            if a[0]<other.punto[0]:
                a[0]=a[0]+1
            if a[1]<other.punto[1]:
                a[1]=a[1]+1
            if a[0]>other.punto[0]:
                a[0]=a[0]-1
            if a[1]>other.punto[1]:
                a[1]=a[1]-1
        b.append(list(a))
        return b
    def distancia(self,other):
        x=self.punto[0]-other.punto[0]
        y=self.punto[1]-other.punto[1]
        z=math.sqrt((x**2)+(y**2))
        return z
if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  print(p1.punto)
  print(p2.punto)
  print(p1.distancia(p2))  
  print(p1.camino(p2))