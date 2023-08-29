#Suma de los N primeros números
n=int(input("ingrese un numero natural: "))
if n>=1:
 n=(n*(n+1))/2
 print(n)
else:
 print("ingrese un numero natural: ")