import math
def area_triangulo(base,altura):
    a=int(base)
    b=int(altura)
    return print("El area de un triangulo de base",a,"y altura",b,"debiera ser",a*b/2)
    pass

def area_rectangulo(base,altura):
    c=int(base)
    d=int(altura)
    areaRectangulo=c*d
    return print(areaRectangulo)
    pass

def area_rombo(diagonal1,diagonal2):
    e=float(diagonal1)
    f=float(diagonal2)
    areaRombo=(e*f)/2
    return print(areaRombo)
    pass

def area_circulo(radio):
    g=float(radio)
    areaCirculo=(math.pi)*g**2
    return print(areaCirculo)
    pass
if __name__ == "__main__":
    ingresarOpcion=input(("ingresar opcion area: "))
    c="circulo"
    t="triangulo"
    r="rectangulo"
    ro="rombo"
    if ingresarOpcion==c:
      area_circulo(input("ingresar radio: "))

    if ingresarOpcion==t:
      resultadoTriangulo=area_triangulo(input("ingresar base: "),input("ingresar altura: "))


    if ingresarOpcion==r:
      resultadoRectangulo=area_rectangulo(input("ingresar base: "),input("ingresar altura: "))

    if ingresarOpcion==ro:
      resultadoRombo=area_rombo(input("ingresar diagonal1: "),input("ingresar diagonal2: "))
    pass
           