import math
def area_triangulo(b,a):
    area = (b*a)/2
    return area
        
def area_rectangulo(b,a):
    area = b*a
    return area
        
def area_rombo(d1,d2):
    area = (d1*d2)/2
    return area
        
def area_circulo(r):
    
    area = math.pi*r**2
    return area
        
if __name__ == "__main__":

    print("1=Triángulo")
    print("2=Rectángulo")
    print("3=Rombo")
    print("4=Círculo")
    a=float(input("Ingrese la figura a la cual desea calcular su área: "))

    if a==1:
        b=float(input("Ingrese la base: "))
        a=float(input("Ingrese la altura: "))
        print("El área es: ",area_triangulo(b,a))
    elif a==2:
        b=float(input("Ingrese la base: "))
        a=float(input("Ingrese la altura: "))
        print("El área es: ",area_rectangulo(b,a))
    elif a==3:
        d1=float(input("Ingrese una diagonal: "))
        d2=float(input("Ingrese la otra diagonal: "))
        print("El área es: ",area_rombo(d1,d2))
    elif a==4:
        r=float(input("Ingrese el radio: "))
        print("El área es: ",area_circulo(r))
    else:
        print("La figura no es válida.")