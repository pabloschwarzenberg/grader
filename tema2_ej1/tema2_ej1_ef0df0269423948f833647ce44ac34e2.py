import math

def area_triangulo(base,altura):
    j = (base * altura)/2 
    print ("el area_triangulo es: ", j)
    return j
    pass

def area_rectangulo(base,altura):
    k = (base * altura)
    print ("el area_rectangulo es: ", k)
    return k
    pass

def area_rombo(diagonal1,diagonal2):
    l = (diagonal1 * diagonal2)/2 
    print ("el area_rombo es: ", l)
    return l
    pass

def area_circulo(radio):
    m = (math.pi * radio**2)
    print ("el area_circulo es: ", m)
    return m
    pass

if __name__ == "__main__":
    x = int(input ("Para calcular area: triangulo presione 1, rectangulo presione 2, rombo presione 3, circulo presione 4: "))
    
    if x == 1: 
            y = int (input ("Ingrese la base del triangulo: "))
            z = int (input ("Ingrese la altura del triangulo: "))
            area_triangulo (y, z)
    elif x == 2: 
            a = int (input ("Ingrese la base del rectangulo: "))
            b = int (input ("Ingrese la altura del rectangulo: "))
            area_rectangulo (a, b)   
    elif x == 3: 
            c = int (input ("Ingrese la diagonal1 del rombo: "))
            d = int (input ("Ingrese la diagonal2 del rombo: "))
            area_rombo (c, d) 
    elif x == 4: 
            e = int (input ("Ingrese el radio del circulo: "))
            area_circulo (e) 
        
    else: print ("opcion mal ingresada, volver a intentarlo: ")
    pass
           