#Suma de los N primeros números
n = eval(input("ingrese el primer numero natural: "))
print(n)
var1 = n*(n+1)/2
var2 = n*(var1+1)/2
print("los primeros numeros naturales son: ", n, var1, var2)
suma = n+var1+var2
print("y su suma es: ", suma)