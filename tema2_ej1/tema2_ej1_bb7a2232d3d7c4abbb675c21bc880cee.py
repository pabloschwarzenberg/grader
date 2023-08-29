def area_triangulo(base,altura):
    pass

def area_rectangulo(base,altura):
    pass

def area_rombo(diagonal1,diagonal2):
    pass

def area_circulo(radio):
    pass

if __name__ == "__main__":
    pass
#elegir un area
print("ingrese figura para sacar su area")
area= (input("(T:Triángulo, C:Ciculo, R:Rectangulo, Ro:Rombo)   "))
print(area)
if area == "T"or "t" :
    base_triangulo= float(input("¿Cual es la base?  "))
    altura_triangulo= float(input("¿Cual es la altura?  "))
    area_triangulo= (base_triangulo*altura_triangulo)/ 2 
    print(f"El area del tríangulo es:{area_triangulo}")
elif area == "C" or "c":
    radio= float(input("¿Cual es el radio? "))
    pi= "pi"
    area_circulo= radio**2 + pi 
    print(f"El area del circulo es: {area_circulo} ")
elif area == "R" or "r" :
    base_rectangulo= float(input("¿Cual es la base?  "))
    altura_rectangulo= float(input("¿Cual es la altura?  "))
    area_rectangulo= (base_rectangulo*altura_rectangulo)
    print(f"El area del rectagulo es {area_rectangulo}")
elif area == "RO" or "Ro" or "rO" or "ro":
    diagonalM= float(input("¿Cual es la diagonal mayor?   "))  
    diagonalMe= float(input("¿Cual es la diagonal menor?  "))
    area_rombo= (diagonalM*diagonalMe)/ 2
    print(f"El area del rombo es  {area_rombo} ")
else:
    print("FIGURA NO VALIDA")         