#Factores Primos
num=int(input("ingrese numero: "))
factor=2
while num>1:
    if num % factor == 0:
        print(factor)
        num //= factor
    else:
        factor += 1    