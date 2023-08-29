#Factores Primos
num = int(input("Ingrese Número: "))

factor=2

while factor<=num:

  if num%factor==0:

    print(factor)

    num = num/factor

  else:

    factor+=1      