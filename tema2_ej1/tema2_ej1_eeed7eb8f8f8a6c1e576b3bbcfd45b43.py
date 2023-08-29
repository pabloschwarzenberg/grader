from math import pi
   
def area_triangulo(base, altura):
    var_AreaTri = (base * altura) / 2
    return var_AreaTri

def area_rectangulo(base, altura):
    var_AreaRec = base * altura
    return var_AreaRec

def area_rombo(diagonal1, diagonal2):
    var_AreaRom = (diagonal1 * diagonal2) / 2
    return var_AreaRom

def area_circulo(radio):
    var_AreaCir = pi * radio ** 2
    return var_AreaCir

if __name__ == "__main__":
    var_Alternativa = -1
    while (var_Alternativa > 4 or var_Alternativa < 0):
        print("Qué desea hacer? Seleccione una alternativa.")
        print("1. Obtener el área de un triangulo")
        print("2. Obtener el área de un rectangulo")
        print("3. Obtener el área de un rombo")
        print("4. Obtener el área de un circulo")
        
        var_Alternativa = int(input("Selecciona una opción: "))
        
        if var_Alternativa == 1:
            area_triangulo(int(input("Ingresa la base: ")), int(input("Ingresa la altura: ")))
        elif (var_Alternativa == 2):
            area_rectangulo(int(input("Ingresa la base: ")), int(input("Ingresa la altura: ")))
        elif (var_Alternativa == 3):
            area_rombo(int(input("Ingresa la diagonal 1: ")), int(input("Ingresa la diagonal 2: ")))
        else:
            area_circulo(int(input("Ingresa el radio: ")))

    pass