def area_triangulo(base, altura):
    return ((base *altura )/2)

def area_rectangulo(base, altura):
    return (base *altura)


def area_rombo(diagonal1, diagonal2):
    return ((diagonal1 *diagonal2 )/2)


def area_circulo(radio):
    import math
    return ((radio** 2) * math.pi)


if __name__ == "__main__":
    seleccion =1
    while seleccion != 0:
        print("Opción 1: Área triangulo\n""Opción 2: Área rectangulo\n""Opción 3: Área rombo\n""Opción 4: Área circulo\n""Para salir presione 0")
        seleccion = eval(input("Ingrese opcion escogida: "))
        if seleccion == 1:
            base_t = float(input("Ingrese base: "))
            altura_t = float(input("Ingrese altura: "))
            areatri = area_triangulo(base_t,altura_t)
            print("el area es:",areatri)

        if seleccion == 2:
            base_r =eval(input("Ingrese base: "))
            altura_r= eval(input("Ingrese altura: "))
            arearec = area_rectangulo(base_r, altura_r)
            print("el area es:",arearec)

        if seleccion == 3:
            diago1 = eval(input("ingrese diagonal1: "))
            diago2 = eval(input("ingrese diagonal2: "))
            arear = area_rombo(diago1, diago2)
            print("el area es:",arear)

        if seleccion == 4:
            rad = eval(input("ingrese radio: "))
            areacir = area_circulo(rad)
            print("el area es:",areacir)
