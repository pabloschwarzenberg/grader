from math import sqrt as r
import math
class Ciudad:
  def __init__(self,x,y):
      self.x=x
      self.y=y
      
  def camino(self,c2):
      a=self.x
      b=self.y
      c=c2.x
      d=c2.y
      j=[]
      if a==c and b==d:
          return("Las ciudades son la misma")
      elif a==c:
          while b!=d:
              b=b+1
              j.append([a,b])
      elif b==d:
          while a!=c:
              a=a+1
              j.append([a,b])
      else:
       VDX=c-a
       VDY=d-b
       if VDX<0 and VDY<0:
           v=-1
       else:
           v=1
       m=float(VDY/VDX)
       if m>0:
        m=m.as_integer_ratio()
        VDY=v*int(m[0])
        VDX=v*int(m[1])
        j=[]
        j.append([a,b])
        g=a+VDX
        h=b+VDY
        if g!=c and h!=d:
          while True:
            if g!=c and h!=d:  
              j.append([g,h])
              g=g+VDX
              h=h+VDY
            else:
                break
          j.append([c,d])
        else:
          j.append([c,d])
       else:
          m=-m
          m=m.as_integer_ratio()
          VDY=-(int(m[0]))
          VDX=int(m[1])
          j=[]
          j.append([a,b])
          g=a+VDX
          h=b+VDY
          if g!=c and h!=d:
            while True:
              if g!=c and h!=d:  
                j.append([g,h])
                g=g+VDX
                h=h+VDY
              else:
                break
            j.append([c,d])
          else:
            j.append([c,d])
      return j
             
          
      
  def distancia(self,c2):
      a=self.x
      b=self.y
      c=c2.x
      d=c2.y
      D=r(((a-c)**2)+((b-d)**2))
      
      return D

if __name__ == "__main__":
  c1=Ciudad(1,1)
  c2=Ciudad(3,3)
  print(c1.distancia(c2)) 
  print(c1.camino(c2))