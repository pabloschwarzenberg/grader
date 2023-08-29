#Suma de los N primeros números
n = int(input("Ingrese un número natural: "))


while (n == n): 
    if (n >= 1):
        suma = (n*(n+1))/2
        suma = round(suma)
        print("La suma de los ",n,"primeros números naturales es: ",suma)
        break
    
    else:
        print("Ese no es un número natural")
        n = int(input("Ingrese un número natural: "))
        suma = (n*(n+1))/2