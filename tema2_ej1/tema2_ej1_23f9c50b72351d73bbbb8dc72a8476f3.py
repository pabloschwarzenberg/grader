from math import pi
def area_triangulo(base,altura):
    area= (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area=(base*altura)
    return area

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2
    return area

def area_circulo(radio):
    area= (radio*radio)*pi
    return area

if __name__ == "__main__":
    def menu():
      print("1. Área triángulo\n""2. Área rectángulo\n""3. Área rombo\n""4. Área círculo\n")
      opcion=input("Ingrese el área que desea calcular: ")
      if opcion==1:
        a=float(input("Ingrese base"))
        b=float(input("Ingrese altura"))
        print(area_tringulo(a,b))
      elif opcion==2:
        a=float(input("Ingrese base"))
        b=float(input("Ingrese altura"))
        print(area_rectangulo(a,b))
      if opcion==3:
        a=float(input("Ingrese diagonal 1"))
        b=float(input("Ingrese diagonal 2"))
        print(area_rombo(a,b))
      if opcion==4:
        a=float(input("Ingrese radio"))
        print(area_circulo(a))
        
           