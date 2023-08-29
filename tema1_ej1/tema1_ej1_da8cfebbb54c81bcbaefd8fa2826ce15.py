#Suma de los N primeros números
n = int(input("Ingrese un número entero positivo: "))
if(n>=1):
    s= n*(n+1)
    s = s//2
    print("El resultado de la suma es:", s)
else:
    if(x<=0):
        print("ERROR, el número ingresado NO es positivo, por favor intente nuevamente: ")
