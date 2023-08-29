import math
def area_triangulo(base,altura):
    b=(base*altura)/2
    print(b)
    return b
def area_rectangulo(base,altura):
    f=base*altura
    print(f)
    return f
def area_rombo(diagonal1,diagonal2):
    f=(diagonal1*diagonal2)/2
    print(f)
    return f
def area_circulo(radio):
    pi=math.pi
    area=pi*(radio**2)
    print(area)
    return(area)
if __name__ == "__main__":
    while True:
        option=0
        print("INGRESA UN NUMERO DEL 0 AL 3 dependiendo de su opcion")
        print("Escoge 0 para calcular area de triangulo:")
        print("Escoge 1 para calcular area de rectangulo:")
        print("Escoge 2 para calcular area de rombo:")
        print("Escoge 3 para calcular area de circulo:")
        option=int(input())      
        if option==0:
            base=int(input())
            altura=int(input())
            area_triangulo(base,altura)
            break
        elif option==1:
            base==int(input())
            altura=int(input())
            area_rectangulo(base,altura)
            break
        elif option==2:
            diagonal1=int(input())
            diagonal2=int(input())
            area_rombo(diagonal1,diagonal2)
            break
        elif option==3:
            radio=int(input())
            area_circulo(radio)
            break
        else:
            print("ingresa un numero del 0 al 3")
