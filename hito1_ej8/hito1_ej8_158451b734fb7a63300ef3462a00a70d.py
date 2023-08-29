#Descomponer un número
num = int(input('Ingresa un número: '))
mile = num / 1000
x = num % 1000
cente = x / 100
x = x % 100
dece = x / 10
uni = x % 10

mile = int(mile)
cente = int(cente)
dece = int(dece)
uni = int(uni)
print(mile,'M +', cente,'C +',dece,'D +',uni,'U')