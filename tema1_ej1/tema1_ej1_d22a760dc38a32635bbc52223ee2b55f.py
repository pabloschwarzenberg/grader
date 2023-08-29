#Suma de los N primeros números
n = int(input("ingrese hasta que numero natural desea que se haga la suma: "))

while n < 0:
    n = int(input("ingrese un numero natural porfavor: "))
print("la suma es: ",n*(n+1)/2)     