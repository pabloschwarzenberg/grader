#Factores Primos
number=int(input("Ingresar numero: "))
f=2
while f<=number:
    if number%f==0:
        print(f)
        number=number/f
    else:
            f+=1