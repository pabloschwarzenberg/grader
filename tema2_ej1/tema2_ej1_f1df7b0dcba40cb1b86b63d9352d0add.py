import math
def area_triangulo(base,altura):
    A=(base*altura)/2
    return A
def area_rectangulo(base,altura):
    A=base*altura
    return A

def area_rombo(diagonal1,diagonal2):
    A=(diagonal1*diagonal2)/2
    return A

def area_circulo(radio):
    A=(math.pi*radio*radio)
    return A
    
if __name__ == "__main__":

    print("[1]:triangulo")
    print("[2]:rectangulo")
    print("[3]:rombo")
    print("[4]:circulo")

    main=int(input("Que quieres hacer:"))
    if(orden==1):
          base=int(input("base:"))
          altura=int(input("altura:"))
          print(area_triangulo(base,altura))
    elif(orden==2):
        base=int(input("base:"))
        altura=int(input("altura:"))
        print(area_rectangulo(base,altura))
    elif(orden==3):
        diagonal1=int(input("diagonal1:"))
        diagonal2=int(input("diagonal2:"))
        print(area_rectangulo(diagonal1,diagonal2))
    elif(orden==4):
        radio=int(input("radio:"))
        print(area_circulo(radio))
                  
           