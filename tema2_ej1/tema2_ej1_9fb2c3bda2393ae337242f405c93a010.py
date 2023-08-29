def area_triangulo(base,altura):
    base=float(base)
    altura=float(altura)
    A=(base*altura)/2
    return A


def area_rectangulo(base,altura):
    base = float(base)
    altura = float(altura)
    A=base*altura
    return A

def area_rombo(diagonal1,diagonal2):
    diagonal1=float(diagonal1)
    diagonal2=float(diagonal2)
    A=(diagonal2*diagonal1)/2
    return A

def area_circulo(radio):
    import math
    radio=float(radio)
    A=math.pi*radio**2
    return A
   

if __name__ == "__main__":
    figura=int(input("Elija el numero de la figura que quiera seleccionar (1: triangulo, 2: rectangulo, 3: rombo, 4: circulo): "))
    if figura==1:
        base=input("Base: ")
        altura=input("Altura: ")
        print ("El area del trianngulo es",area_triangulo(base,altura))
    if figura==2:
        base = input("Base: ")
        altura = input("Altura: ")
        print ("El area del rectangulo es", area_rectangulo(base, altura))
    if figura==3 :
        diagonal1=input("Diagonal 1: ")
        diagonal2=input("Diagonal 2: ")
        print ("El area del rombo es", area_rombo(diagonal1,diagonal2))
    if figura==4 :
        radio=input("Radio: ")
        print ("El area del circulo es", area_circulo(radio))
    
           