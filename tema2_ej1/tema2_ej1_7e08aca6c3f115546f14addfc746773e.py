pi=3.14

def area_triangulo(base,altura):
    resultado1=(base*altura)/2
    return(resultado1)

def area_rectangulo(base,altura):
    resultado2=base*altura
    return(resultado2)

def area_rombo(diagonal1,diagonal2):
    resultado3=(diagonal1*diagonal2)/2
    return(resultado3)

def area_circulo(radio):
    resultado4=pi*radio**2
    return(resultado4)

base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
salida1=area_triangulo(base,altura)
print("El area del triangulo es:", round(salida1 ))

salida2=area_rectangulo(base,altura)
print("El area de rectangulo es:", round(salida2) )

diagonal1=float(input("Ingrese diagonal 1: "))
diagonal2=float(input("Ingrese diagonal 2: "))
salida3=area_rombo(diagonal1,diagonal2)
print("El area del rombo es:", round(salida3))

radio=float(input("Ingrese el radio del circulo: "))
salida4=area_circulo(radio)
print("El area del circulo es: ", round(salida4))

           