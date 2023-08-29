import math
def area_triangulo(base,altura):
    calculo1=(base*altura)/2
    return calculo1
def area_rectangulo(base,altura):
    calculo2=base*altura
    return calculo2
def area_rombo(diagonal1,diagonal2):
    calculo3=(diagonal1*diagonal2)/2
    return calculo3  
def area_circulo(radio):
    calculo4=math.pi*radio**2
    return calculo4

if __name__ == "__main__":
    figura=input('que quieres calcular?(triangulo=1,rectangulo=2,rombo=3,circulo=4:')
    if figura==1:
      area_triangulo(base,altura)
    if figura==2:
      area_rectangulo(base,altura)
    if figura==3:
      area_rombo(diagonal1,diagonal2)
    if figura==4:
      area_circulo(radio)
    
           