def descomponer(n):
    primos=[]
    for m in range(2,n+1):
        while n%m ==0:
            primos.append(m)
            n = n/m
    return primos
n = int(input("ingrese el valor a descomponer; "))
primos = descomponer(n)
print(primos)