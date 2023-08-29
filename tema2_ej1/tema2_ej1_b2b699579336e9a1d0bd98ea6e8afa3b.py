from math import pi

def area_triangulo(base,altura):
    area_t = base * altura/2
    return (area_t)

def area_rectangulo(base,altura):
    area_r = base * altura
    return(area_r)
    

def area_rombo(diagonal1,diagonal2):
    area_ro = diagonal1 * diagonal2 / 2
    return(area_ro)

def area_circulo(radio):
    area_c = pi* (radio**2)
    return(area_c)
    

if __name__ == "__main__":
    print("1: triangulo")
    print("2: rectangulo")
    print("3: rombo")
    print("4: circulo")
    x = int(input("seleccione figura: "))
    if x == 1:
        base = int(input("base triangulo: "))
        altura = int(input("altura triangulo: "))
        print (area_triangulo(base,altura))
    elif x == 2:
        base = int(input("base rectangulo: "))
        altura = int(input("altura rectangulo: "))
        print (area_rectangulo(base,altura))
    elif x == 3:
        diagonal_1 = int(input("diagonal1: "))
        diagonal_2 = int(input("diagonal2: "))
        print (area_rombo(diagonal_1,diagonal_2))
    elif x == 4:
        rad = int(input("radio: "))
        print (area_circulo(rad))
       
