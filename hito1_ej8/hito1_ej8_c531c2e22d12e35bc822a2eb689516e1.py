#Descomponer un número
numero = int(input("Ingrese un numero de hasta cuatro digitos: "))

a = []

M = numero / 1000
tmp = numero % 1000
a.append('%i' %M)

C = tmp / 100
tmp = tmp % 100
a.append('%i' %C)

D = tmp / 10
a.append('%i' %D)

U = tmp % 10
a.append('%i' %U)


print(a[0],'M + ',a[1],'C + ',a[2],'D + ',a[3],'U')