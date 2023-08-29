import math
def area_triangulo(base,altura):
  areat=(base*altura)/2
  return(areat)
  
def area_rectangulo(base,altura):
  arear=base*altura
  return(arear)

def area_rombo(diagonal1,diagonal2):
  aread=(diagonal1*diagonal2)/2  
  return(aread)
  
def area_circulo(radio):
  areac= (math.pi)*radio*radio
  return(areac)

if __name__ == "__main__":
    pass
           