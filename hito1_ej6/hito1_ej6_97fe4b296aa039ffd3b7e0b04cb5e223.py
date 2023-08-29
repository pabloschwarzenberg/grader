#Ordenar tres números

numero1=eval(input('Ingresa un primer numero: '))
numero2=eval(input('Ingresa un segundo numero: '))
numero3=eval(input('Ingresa un tercer numero: '))

if numero1 <= numero2 <= numero3:
    print('El orden es: ', numero1, ',', numero2,',', numero3)
if numero1 <= numero3 <= numero2:
    print('El orden es: ', numero1, ',', numero3,',', numero2)
if numero2 <= numero1 <= numero3:
    print('El orden es: ', numero2, ',', numero1,',', numero3)
if numero3 <= numero1 <= numero2:
    print('El orden es: ', numero3,',', numero1,',', numero2)
if numero2 <= numero3 <= numero1:
    print('El orden es: ', numero2,',', numero3,',', numero1)
if numero3 <= numero2 <= numero1:
    print('El orden es: ', numero3,',', numero2,',', numero1)