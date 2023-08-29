import math
def area_triangulo():
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    areaTri = (base*altura)/2
    print(areaTri)
    pass
def area_rectangulo():    
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    areaRec = (base*altura)
    print(areaRec)
    pass
def area_rombo():
    diagonal1 = int(input("Diagonal 1: "))
    diagonal2 = int(input("Diagonal 2: "))
    areaRom = (diagonal1*diagonal2)/2
    print(areaRom)
    pass
def area_circulo():
    radio = int(input("Radio: "))
    areaCir = (math.pi*radio*radio)
    print(areaCir)
    pass
if __name__ == "__main__":
    area_triangulo()
    area_rectangulo()        
    area_rombo()    
    area_circulo()
    pass