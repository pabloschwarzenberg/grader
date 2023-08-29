class Ciudad:
  def __init__(self,coor1,coor2):
    self.coor1=coor1
    self.coor2=coor2
  def camino(self,coor1):
    lista=[]
    lista=lista.append(coor1)
    flag=0
    while flag==0:
      if self.coor1[0] == self.coor2[0]:
        if self.coor1[1]>self.coor2[1]:
          nueva_coor=self.coor1[1]+1
          lista=lista.append(nueva_coor)
          flag=0
        elif coor[1]<coor2[1]:
          nueva_coor=coor1[1]-1
          lista=lista.append(nueva_coor)
          flag=0
        elif coor1[1]==coor2[1]:
          lista=lista.append(coor2)
          flag=1
      elif coor1[1]==coor2[1]:
        if coor1[0]>coor2[0]:
          nueva_coor=coor1[0]-1
          lista=lista.append(nueva_coor)
          flag=0
        elif coor1[0]<coor2[0]:
          nueva_coor=coor1[0]+1
          lista=lista.append(nueva_coor)
          flag=0
      return(lista)

  def distancia(self):
    distance=((coor2[0]-coor1[0])**2+(coor2[1]-coor1[0])**2)**(1/2)
    return distance
  
         