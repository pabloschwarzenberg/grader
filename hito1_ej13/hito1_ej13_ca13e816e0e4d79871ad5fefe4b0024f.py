#Factores Primos
n=2
number=int(input('ingrese el número que desea descomponer en factores primos: '))
while number!=1:
    if number%n==0:
        print(n)
        number=number/n
    else:
        n+=1