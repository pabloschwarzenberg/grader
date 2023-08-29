#Cálculo del dígito verificador de un rut
      

num = input('\nIngresa un número: ')
l_num = []
num_multi = 1
suma1 = 0

for i in num:
    l_num.append(i)

l_num2 = list(reversed(l_num))

for i in l_num2:
    i = int(i)
    if num_multi==7:
        num_multi = 1
    num_multi = num_multi+1
    suma = i*num_multi
    suma1 = suma1+suma

div = suma1/11
entero = int(div)
calculo = suma1-(11*entero)
num_veri = 11-calculo

if num_veri==11:
    num_veri = 0
elif num_veri==10:
    num_veri = 'k'

print('\n', 'dv=', num_veri)