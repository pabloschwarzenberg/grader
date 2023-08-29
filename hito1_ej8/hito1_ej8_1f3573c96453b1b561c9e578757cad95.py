#Descomponer un número
numero = int(input('Introduce un número: '))

milesimas = numero/1000
tmp = numero%1000

centesimas = tmp/100
tmp = numero%100

decenas = tmp/10
unidades = tmp%10

print('M:%i' % milesimas)
print('C:%i' % centesimas)
print('D:%i' % decenas)
print('U:%i' % unidades)

if milesimas<=0:
  print(centenas, 'C+', decenas, 'D+', unidades, 'U')
  if centenas<=0:
    print(decenas, 'D+', unidades, 'U')
    if decenas<0:
      print(unidades,'U')
if milesimas>0:
  print('%i' % milesimas, 'M+', '%i' % centesimas, 'C+' , '%i' % decenas, 'D+', '%i' % unidades, 'U')