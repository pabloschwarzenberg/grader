 
 if __name__ == "__main__": 
 
 
 base_t=float(input("ingrese base del triangulo en cm:"))
 altura_t=float(input("ingrese altura del triangulo en cm:"))
 base_re=float(input("ingrese base rectangulo en cm:"))
 altura_re=float(input("ingrese altura del rectangulo en cm:"))
 diagonal_1=float(input("ingrese diagonal 1 del rombo:"))
 dagonal_2=float(input("ingrese diagonal 2 del rombo:"))
 radio_1=float(input("ingrese radio del circulo:"))

def area_triangulo(base_t,altura_t):
  while base_t and altura_t > 0:
    area=(base_t*altura_t)/2
    print(area)

def area_rectangulo(base_re,altura_re):
    while base_re and altura_re >0:
      area_2=(base_re*altura_re)
      print(area_2)

def area_rombo(diagonal_1,diagonal_2):
    while diagonal_1 and diagonal_2>0:
      area_3=(diagonal_1/diagonal_2)/2
      print(area_3)

def area_circulo(radio_1):
  while radio_1>0:   
   area_4=(radio_1**2)
   print(area_4)

           