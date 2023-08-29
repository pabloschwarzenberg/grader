#Suma de los N primeros números
def suma(n) :
    n=n
    m=n+1
    return n*m/2
    
numero=input("Ingrese un número: ")
numero=eval(numero)
suma = suma(numero)
print("La suma de los primeros",numero,"numeros es",suma)