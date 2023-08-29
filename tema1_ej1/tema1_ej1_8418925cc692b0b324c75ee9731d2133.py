#Suma de los N primeros números
n=0
n=int(input("Ingrese un número natural:"))
if(n>0):
    s=(n*(n+1)/2)
    print("La suma es:",s)
else:
    print("Esta malo el número ingresado")