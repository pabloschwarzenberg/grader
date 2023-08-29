class Ciudad:
  import math
  def distancia(x1,y1,x2,y2):
     return  math.sqrt((x1-x2)**2+(y1-y2)**2)
  a_x  =  1
  a_y  =  1
  k_x  =  3
  k_y  =  3
  dist  =  distancia(a_x,a_y,k_x,k_y)
  print(“La distancia es “, dist) 