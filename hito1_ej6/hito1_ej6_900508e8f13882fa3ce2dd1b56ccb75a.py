#Ordenar tres números
numero1 = eval(input('Escriba el primer número de tres: '))
numero2 = eval(input('Escriba el segundo número de tres: '))
numero3 = eval(input('Escriba el trecer número de tres: '))

if numero1 <= numero2 <= numero3:
    print('EL orden es: ', numero1, ', ', numero2, ', ', numero3)
if numero1 <= numero3 <= numero2:
    print('EL orden es: ', numero1, ', ', numero3, ', ', numero2)

if numero2 <= numero1 <= numero3:
    print('EL orden es: ', numero2, ', ', numero1, ', ', numero3)
if numero2 <= numero3 <= numero1:
    print('EL orden es: ', numero2, ', ', numero3, ', ', numero1)

if numero3 <= numero2 <= numero1:
    print('EL orden es: ', numero3, ', ', numero2, ', ', numero1)
if numero3 <= numero1 <= numero2:
    print('EL orden es: ', numero3, ', ', numero1, ', ', numero2)
