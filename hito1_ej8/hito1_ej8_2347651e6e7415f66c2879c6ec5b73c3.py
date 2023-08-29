n=int(input("Ingrese el numero entero de 4 cifras: "))
n_original=n

un=n%10
n=n//10
dc=n%10
n=n//10
cen=n%10
n=n//10
unM=n%10

print("Descomposición: ",unM,"M +", cen,"C +", dc,"D +", un,"U")
