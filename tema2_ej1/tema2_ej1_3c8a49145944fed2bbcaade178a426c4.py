import math
def area_triangulo(base,altura):
    area= (base*altura)/2
    return area

def area_rectangulo(base,altura):
    area= base*altura
    return area

def area_rombo(d1,d2):
    area= (d1*d2)/2
    return area

def area_circulo(radio):
    area= math.pi*((radio)**2)
    return area
    
if __name__ == "__main__":
    print("/n Escoja cual es la figura a la cual desea calcular su area: /n"
          "1) rectangulo /n"
          "2) triangulo /n"
          "3) rombo /n"
          "4) circulo /n")
    i= int(input("Ingrese su opcion: "))
    if i==1:
        ancho= float(input("Ingrese el ancho del rectangulo"))
        lado= float(input("Ingrese el largo del rectangulo"))
        a= area_rectangulo(ancho, lado)
        print(a)
    if i==2:
        base= float(input("Ingrese el largo del lado base"))
        altura= float(input("Ingrese el largo del lado altura"))
        b= area_triangulo(base,altura)
        print(b)
    if i==3:
        d1= float(input("Ingrese el ancho del rombo"))
        d2= float(input("Ingrese el largo del rombo"))
        c= area_rombo(d1,d2)
        print(c)
    if i==4:
        radio= float(input("Ingrese radio del circulo"))
        d= area_circulo(radio)
        print(d)
           