from math import sqrt

class Ciudad:
  def __init__(self,x,y):
    self.x=x
    self.y=y

def camino(p1,p2):

    x=str(int((p1.x + p2.x)/2))
    y=str(int((p1.y + p2.y)/2))

    
    px1=(str(p1.x))
    py1=(str(p1.y))
    punto1=px1+','+py1
   

    puntoM=x+','+y

    
    px2=(str(p2.x))
    py2=(str(p2.y))
    punto2=px2+','+py2

    
    caminoOK=[punto1,puntoM,punto2]
    return caminoOK

def distancia(p1,p2):
   
    st=str(sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2))
    st=st[0:4]
    return float(st)

if __name__ == "__main__":

    p1 = Ciudad(1,1)
    p2 = Ciudad(3,3)
    
    print(camino(p1,p2))
    print(distancia(p1,p2))
    
         