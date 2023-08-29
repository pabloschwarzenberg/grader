#Factores Primos
num = int(input("Ingrese un numero: "))
j=2
while j<=num:
    if num%j==0:
        print(j)
        num = num/j
    else:
        j+=1      