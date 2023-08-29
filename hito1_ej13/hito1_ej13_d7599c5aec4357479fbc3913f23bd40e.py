#Factores Primos
n = int(input("Ingrese un número entero:"))
d = int(2)
while (n!=1):
    if (n%d==0):
        print(str(d)+"")
        n = n/d
    else:
        d=d+1