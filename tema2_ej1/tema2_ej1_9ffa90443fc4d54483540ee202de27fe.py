from math import pi

# tienes que sacar areas, no olvidar
#b = base, a = altura, bruh = area, r = radio

def area_rectangulo(b, a):
    bruh = b*a
    return bruh
def area_triangulo(b, a):
    bruh = (b*a)/2
    return bruh
def area_rombo(dmay, dmin):
    bruh = (dmay*dmin)/2
    return bruh
def area_circulo(r):
    bruh = pi*r**2
    return bruh

print("menu: ")
print("1: rectangulo")
print("2: triangulo")
print("3: rombo")
print("4: circulo")
print("0: salir")

if __name__ == "__main__":

    menu = int(input("1, 2, 3, 4, 0: "))

    while menu == 0:
        print("hasta la proxima!")
        break
    while menu == 1:
        b = float(input("porfavor indique la base: "))
        a = float(input("porfavor indique la altura: "))
        print(area_rectangulo(b, a))
        break
    while menu == 2:
        b = float(input("porfavor indique la base: "))
        a = float(input("porfavor indique la altura: "))
        print(area_triangulo(b, a))
        break
    while menu == 3:
        dmay = float(input("porfavor indique la diagonal mayor: "))
        dmin = float(input("porfavor indique la diagonal menor: "))
        print(area_rombo(dmay, dmin))
        break
    while menu == 4:
        r = float(input("porfavor indique el radio: "))
        print(area_circulo(r))
        break