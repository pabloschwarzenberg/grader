numero = int(input('Ingresa un numero: '))
i = 1
acumulador = 0
while i < numero:
    if numero%i == 0:
        acumulador = acumulador + i
    i = i+1
if acumulador == numero:
    print('true')
else:
    print('false')


          