#Factores Primos

n = int(input("Ingrese numero entero: "))


for s in range(2,n+1):
    while n%s == 0:
        print(s)
        n = n/s
        