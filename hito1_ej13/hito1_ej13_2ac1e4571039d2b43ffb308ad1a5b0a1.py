#Factores Primos
num=int(input("ingresar numero: "))
y=2
while y<=num:
    if num%y==0:
        print(y)
        num=num/y
    else:
            y+=1
