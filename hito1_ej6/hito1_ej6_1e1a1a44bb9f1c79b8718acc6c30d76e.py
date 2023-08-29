#Ordenar tres números
numero1 = eval(input('Ingrese el primer número de tres: '))
numero2 = eval(input('Ingrese el segundo número de tres: '))
numero3 = eval(input('Ingrese el tercer número de tres: '))

if numero1 <= numero2 <= numero3:
    print('El orden es: ', numero1, ', ', numero2, ', ', numero3)
if numero1 <= numero3 <= numero2:
    print('El orden es: ', numero1, ', ', numero3, ', ', numero2)
if numero2 <= numero1 <= numero3:
    print('El orden es: ', numero2, ', ', numero1, ', ', numero3)
if numero2 <= numero3 <= numero1:
    print('El orden es: ', numero2, ', ', numero3, ', ', numero1)
if numero3 <= numero1 <= numero2:
    print('El orden es: ', numero3, ', ', numero1, ', ', numero2)
if numero3 <= numero2 <= numero1:
    print('El orden es: ', numero3, ', ', numero2, ', ', numero1)