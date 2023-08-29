from math import pi

def area_triangulo(base,altura):
    Area=base*altura/2
    return Area

def area_rectangulo(base,altura):
    Area=base*altura
    return Area

def area_rombo(diagonal1,diagonal2):
    Area=diagonal1*diagonal2/2
    return Area

def area_circulo(radio):
    Area= pi*(radio*radio)
    return Area

print("Bienvenido a la Calculadora de Áreas. ¿Qué Área deseas Calcular?")

if __name__ == "__main__":
    menu=int(input("(1) Triagulo\n(2) Rectangulo\n(3) Rombo\n(4) Circulo"))

    if menu==1:
      base=float(input("ingrese base: "))
      altura=float(input("ingrese altura: "))
      area=area_triangulo(base,altura)
      print("El área es: ",area)

    elif menu==2:
        base=float(input("ingrese base: "))
        altura=float(input("ingrese altura: "))
        area=area_rectangulo(base,altura)
        print("El área es: ",area)

    elif menu==3:
          diagonal_M=float(input("ingrese diagonal mayor: "))
          diagonal_m=float(input("ingrese diagonal menor: "))
          area=area_rombo(diagonal_M,diagonal_m)
          print("El área es: ",area)

    elif menu==4:
            radio=float(input("ingrese radio: "))
            area=area_circulo(radio)
            print("El área es: ",area)

    else:
           print()
           print("Tenias 4 opciones, elegiste mal, chao por hilary clinton")


