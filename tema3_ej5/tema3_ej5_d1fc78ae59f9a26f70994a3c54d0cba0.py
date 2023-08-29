class Ciudad:
  def __init__(self,x,y):
      self.coordenadax=x
      self.coordenaday=y
  def __int__(self):
      s= [self.cordenadax,self.coordenaday]
      return s
def pasos(p1,p2):
    if isinstance(p1)=Ciudad and isinstance(p2)=Ciudad:
        distancia= (p2.coordenadax-p1.cordenadax)**2+(p2.coordenaday-p1.coordenaday)**2
        distancia2=(distancia)**(1/2)
        return distancia2  
    else:
         return False
    
if __name__ == "__main__":
  pass
         