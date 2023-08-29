def area_triangulo(base,altura):
    area1=(base*altura)/2
    return area1

def area_rectangulo(base,altura):
    area2=(base*altura)
    return area2

def area_rombo(diagonal1,diagonal2):
    area3=(diagonal1*diagonal2)/2
    return area3

def area_circulo(radio):
    area4=3.14*radio*radio
    return area4
    

print("Ingrese el area que desea calcular: ")
print("Triangulo(1) ")
print("Rectangulo(2) ")
print("Rombo(3)  ")
print("Circulo(4) ")
#resultados 
figura= int(input())
if figura==1:
        base=int(input("Ingrese la base: "))
        altura=int(input("Ingrese la altura: "))
        print(area_triangulo(base,altura))
elif figura==2:
        base2=int(input("Ingrese la base: "))
        altura2=int(input("Ingrese la Altura: "))
        print(area_rectangulo(base2,altura2))
elif figura==3:
        diagonal1=int(input("Ingrese la primera diagonal: "))
        diagonal2=int(input("Ingrese la segunda diagonal: "))
        print(area_rombo(diagonal1,diagonal2))
elif figura==4:
        radio=int(input("Ingrese el radio : "))
        print(area_circulo(radio))
  

           