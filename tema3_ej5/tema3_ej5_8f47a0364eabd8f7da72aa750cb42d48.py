class Ciudad:
  def __init__(self,coordenada1,coordenada2):
    self.coordenada1=coordenada1
    self.coordenada2=coordenada2
  def pasos(self,otro):
    lista_pasos=[]
    lista_pasos.append([self.coordenada1,self.coordenada2])
    if int(self.coordenada1)!=int(otro.coordenada1) or int(self.coordenada2)!=int(otro.coordenada2):
      self.coordenada1+=1
      self.coordenada2+=1
      lista_pasos.append([self.coordenada1,self.coordenada2])
    lista_pasos.append([otro.coordenada1,otro.coordenada2])
    return lista_pasos
    
  def distancia(self,otro):
    distancia_x=(int(otro.coordenada1)-int(self.coordenada1))^2
    distancia_y=(int(otro.coordenada2)-int(self.coordenada2))^2
    distancia_total=(distancia_x+distancia_y)^(1/2)
if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)
  print(p1.pasos(p2))
  print(p1.distancia(p2))