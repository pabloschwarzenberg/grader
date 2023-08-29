from math import sqrt

class Ciudad:
  def _init_(self,x,y):
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

    camino = (f'[[{punto1}],[{puntoM}],[{punto2}]]')
    
    return camino

def distancia(p1,p2):
   
    st=str(sqrt((p1.x - p2.x)*2 + (p1.y - p2.y)*2))
    st=st[0:4]
    return st

if _name_ == "_main_":

    Ciudad1 = Ciudad(1,1)
    Ciudad2 = Ciudad(3,3)
    

    print(distancia(Ciudad1,Ciudad2))
    print(camino(Ciudad1,Ciudad2))