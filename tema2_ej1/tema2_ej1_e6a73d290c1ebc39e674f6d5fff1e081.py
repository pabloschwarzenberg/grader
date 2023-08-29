def area_triangulo(base,altura):
    result = (base*altura)/2
    return result

def area_rectangulo(base,altura):
    result = (base * altura)
    return result

def area_rombo(diagonal1,diagonal2):
    result = (diagonal1*diagonal2 )
    return result

def area_circulo(radio):
     pi = 3,14
     result = (pi*(radio**2))
     return result

ejercicio = str(input('''escoja el tipo de ejercicio:     
                      a) area de un triangulo 
                      b) area de un retangulo 
                      c) area de un rombo 
                      d) area de un circulo :'''))
if ejercicio == "a":
     base = int(input("ingrese base:"))
     altura = int(input("ingrese altura:"))
     result = area_triangulo(base,altura)
     print(result)

if ejercicio == "b":
     base = int(input("ingrese base:"))
     altura = int(input("ingrese altura:"))
     result = area_rectangulo(base,altura)
     print(result)

if ejercicio == "c":
    diagonal1 = int(input("ingrese diagonal1:"))
    diagonal2 = int(input("ingrese diagonal2:"))
    result = area_rombo(diagonal1, diagonal2)
    print(result)

if ejercicio == "d":
    radio = int(input("ingrese el radio:"))
    result = area_circulo(radio)
    print(result)
           