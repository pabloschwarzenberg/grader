import math
def area_triangulo(base,altura):
    t_a=(base*altura)/2
    return t_a
def area_rectangulo(base,altura):
    r_a=base*altura
    return r_a
def area_rombo(diagonal1,diagonal2):
    ro_a=(diagonal1*diagonal2)/2
    return ro_a
def area_circulo(radio):
    c_r=math.pi*(radio*radio)
    return c_r      
if __name__ == "__main__":
    while True:       
        print("1.-Area de un triangulo")
        print("2.-Area de un rectangulo ")
        print("3.-Area de un rombo")
        print("4.-Area de un circulo")
        op=int(input("Escoger una opcion "))
        if op == 1:
            b=int(input("Ingresar base "))
            a=int(input("Ingresar altura " ))
            area_triangulo(a,b)
            print(area_triangulo(a,b))
            continue
        if op == 2:
            b2=int(input("Ingresar base "))
            a2=int(input("Ingresar altura "))
            area_rectangulo(a2,b2)
            print(area_rectangulo(a2,b2))
            continue
        if op == 3:
            d1=int(input("Ingresar diagonal 1 "))
            d2=int(input("Ingresar diagonal 2 "))
            area_rombo(d1,d2)
            print(area_rombo(d1,d2))
            continue
        if op == 4:
            r=int(input("Ingresar radio"))
            area_circulo(r)
            print(area_circulo(r))
            continue  
        pass


           