import math
class Ciudad:
  def __init__(self,posicionx,posiciony):
    self.posicionx=posicionx
    self.posiciony=posiciony
    
  def camino(self,otra):
    a=self.posicionx
    b=self.posiciony
    lista_4=[]
    lista_1=[self.posicionx,self.posiciony]
    lista_3=[otra.posicionx,otra.posiciony]
    lista_4.append(lista_1)
    c=(otra.posicionx-self.posicionx)
    if (otra.posicionx-self.posicionx)!=(otra.posiciony-self.posiciony):
      while a!=b:
        if a>b:
          b+=1
        elif a<b:
          a+=1
        lista_4.append([a,b])

    for i in range(c-1):
      a+=1
      b+=1
      lista_4.append([a,b])
    lista_4.append(lista_3)
    return lista_4
    
  def distancia(self,ciudad):
    self.posicionx-=ciudad.posicionx
    self.posiciony-=ciudad.posiciony
    distancia=math.sqrt(self.posicionx**2+self.posiciony**2)
    dist=distancia
    self.distancia=dist
    return self.distancia

  def __str__(self):
    stposicionx=str(self.posicionx)
    stposiciony=str(self.posiciony)
    return stposicionx+","+stposiciony

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  p1.camino(p2)
  p1.distancia(p2)         