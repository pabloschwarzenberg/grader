from math import pi

def area_triangulo(b,h):

  area=(b*h)/2
  
  return (area)
  
def area_rectangulo(b,h):

  area=(b*h)
  
  return (area)
  
def area_rombo(diag1,diag2):

  area=(diag1*diag2)/2
  
  return (area)
  
def area_circulo(radio):

  area=(pi*radio**2)
  
  return (area)
  
if __name__=="__main__":

  print("menu")
  
  opc=int(input("ingresa 1 para area de triangulo, 2 para area de rectangulo, 3 para area de rombo, 4 para area de circulo o ingresa 0 para salir: "))
  
  while(opc==0):
  
    print("gracias por ocupar calculadora geometrica")
    
    break
    
  while(opc==1):
  
    b=float(input("ingresa la base: "))
    
    h=float(input("ingresa la altura: "))
    
    print(area_triangulo(b,h))
    
    break
    
  while(opc==2):
  
    b=float(input("ingresa la base: "))
    
    h=float(input("ingresa la altura: "))
    
    print(area_rectangulo(b,h))
    
    break
    
  while(opc==3):
  
    diag1=float(input("ingresa la 1era diagonal: "))
    
    diag2=float(input("ingresa la 2nda diagonal: "))
    
    print(area_rombo(diag1,diag2))
    
    break
    
  while(opc==4):
  
    radio=float(input("ingresa radio del circulo: "))
    
    print(area_circulo(radio))
    
    break
           