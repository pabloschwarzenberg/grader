import math 
def area_triangulo(base,altura):
    area=base * altura / 2
    return area 
    
def area_rectangulo(base,altura):
    area= base * altura
    return area

def area_rombo(diagonal1,diagonal2):
    area= diagonal1 * diagonal2 /2
    return area

def area_circulo(radio):
    valorpi= math.pi
    area = valorpi * radio * radio
    return area

if __name__ == "__main__":
  s = int(input("Ingrese un numero"))
  resultado=""
  if s ==1:
    in1=int(input("Ingrese la base del triangulo"))
    in2=int(input("Ingrese la altura del triangulo"))
    resultado= area_triangulo(in1,in2)
    
  elif s==2:    
     in1=int(input("Ingrese la base del rectangulo"))
     in2=int(input("Ingrese la altura del rectangulo"))
     resultado= area_rectangulo(in1,in2)
    
  elif s==3:    
    in1=int(input("Ingrese la diagonal 1 del rombo"))
    in2=int(input("Ingrese la diagonal 2 del rombo"))
    resultado= area_rombo(in1,in2)    

  elif s==4:
    in1=int(input("Ingrese el radio del circulo"))
    resultado= area_circulo(in1)

  else:
    print("No se acepta el numero ingresado")
    resultado="error"   

if __name__ == "__main__":
  print(resultado) 
           