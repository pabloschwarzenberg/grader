print("Elije uno")
print("1. area de triangulo ")
print("2. area de rectangulo ")
print("3. area de rombo ")
print("4. area de circulo ")

n = int(input("ingrese una opcion: "))

if n == 1:
    b = int(input("ingrese base: "))
    a = int(input ("ingrese altura: "))

    def area_triangulo(b, a):
        z = ((b * a) / 2)
    
        return z

    resultado = area_triangulo(b,a)

    print (resultado)

elif n == 2:
    b = int(input("ingrese base: "))
    a = int(input ("ingrese altura: "))

    def area_rectangulo(b, a):
        z = (b * a)
    
        return z

    resultado = area_rectangulo(b,a)

    print (resultado)

elif n == 3:
    b = int(input("ingrese diagonal 1: "))
    a = int(input ("ingrese diagonal 2: "))

    def area_rombo(b, a):
        z = ((b * a) / 2) * 4
    
        return z

    resultado = area_rombo(b,a)

    print (resultado)

elif n == 4 and n <= 4:
    r = int(input("Ingrese radio: "))
    pi = 3.14
    def area_circulo(r):
        area =(pi * (r)**2)
        return area

    resultado = area_circulo(r)

    print (resultado)
           