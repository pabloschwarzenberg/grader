
  
class Ciudad:
     def __init__(self,x,y):
          self.x=x
          self.y=y

     def camino(self,p2):
          x=self.x
          y=self.y
          pasos=[]
          pasos.append([x,y])
          while x!=p2.x or y!=p2.y:
               if x<p2.x:
                    x+=1
               if x>p2.x:
                    x-=1
               if y<p2.y:
                    y+=1
               if y>p2.y:
                    y-=1
               pasos.append([x,y])
               
          return pasos


     def distancia(self,p2):
          x=p2.x
          y=p2.y
          dist=((((x-self.x)**2)+((y-self.y)**2))**(1/2))
          return dist

     def __str__(self):
          return "[{0},{1}]".format(self.x,self.y)
     pass

if __name__ == "__main__":
  p1=Ciudad(1,1)
  p2=Ciudad(3,3)

  print("Camino: ",p1.camino(p2))
  print("Distancia: ",p1.distancia(p2))
  pass
         