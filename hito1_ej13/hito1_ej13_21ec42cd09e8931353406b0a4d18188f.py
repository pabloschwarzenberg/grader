#Factores Primos
P=2
number=int(input('ingrese el número que desea descomponer en factores primos: '))
while number!=1:
    if number%P==0:
        print(P)
        number=number/P
    else:
        P+=1      