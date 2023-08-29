#Conversión de Decimal a Binario
      
n = int(input('\nIngrese un número: '))
print('\n')
l_num = []

while n>0:
    bi = n%2
    l_num.append(bi)
    n = n//2

l_bi = list(reversed(l_num))
print('resultado=', end='')

for i in l_bi:
    print(i, end='')