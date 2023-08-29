#Suma de los N primeros números
n=int(input())
a= int(n*(n+1))/2
if n<=0:
    print("porfavor ingrese un numero positivo")
else:
    print(int(a))