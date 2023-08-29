#Factores Primos
a=2
number=int(input('ingresa el número para convertir en factores primos: '))
while number!=1:
    if number%a==0:
        print(a)
        number=number/a
    else:
        a+=1