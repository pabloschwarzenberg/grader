#Factores Primos
n = int(input("Ingrese un numero: "))
p = 2


while n > 1:
    if n%p == 0:
        print(p)
        n = n/p
        p = 2
    else:
        p += 1