#Suma de los N primeros números
def suma_naturales(kiki):
    suma = kiki * (kiki + 1) // 2
    return suma
 
 N = int(input("Ingrese el número N: "))
 
 suma_naturales(N)