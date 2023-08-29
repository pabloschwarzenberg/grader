numero1 = int(input('Ingrese un numero: '))
numero2 = int(input('Ingrese un numero: '))
numero3 = int(input('Ingrese un numero: '))

if numero1 > numero2 > numero3:
    print('El orden de menor a mayor es: ', numero3, ',' , numero2 , ',' , numero1)

if numero2 > numero3 > numero1:
    print('El orden de menor a mayor es: ', numero1, "," , numero3, ',' , numero2)

if numero3 > numero1 >numero2:
    print('El orden de menor a mayor es: ', numero2, "," , numero1, "," , numero3)

if numero2 < numero3 < numero1:
    print('El orden de menor a mayor es: ', numero2, "," , numero3, "," , numero1)

if numero1 <numero2 < numero3:
    print('El orden de menor a mayor es: ', numero1, "," , numero2, "," , numero3)

if numero3 < numero1 < numero2:
    print('El orden de menor a mayor es: ', numero3, "," , numero1, "," , numero2)

if numero1 == numero2 < numero3:
    print('El orden de menor a mayor es: ', numero1, ',' , numero2, ',' , numero3)

if numero2 == numero3 < numero1:
    print('El orden de menor a mayor es: ', numero2, ',' , numero3, ',' , numero1)

if numero3 == numero1 < numero2:
    print('El orden de menor a mayor es: ', numero3, ',' , numero1, ',' , numero2)

if numero1 == numero2 > numero3:
    print('El orden de menor a mayor es: ', numero3, ',' , numero2, ',' , numero1)

if numero2 == numero3 > numero1:
    print('El orden de menor a mayor es: ', numero1, ',' , numero3, ',' , numero2)

if numero3 == numero1 > numero2:
    print('El orden de menor a mayor es: ', numero2, ',' , numero1, ',' , numero3)

