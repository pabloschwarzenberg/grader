#Factores Primos
n = int(input("Ingrese un número: "))
x = 2
while n > 1:
    if n % x==0:
        print(x)
        n //= x

    else:
        x +=1