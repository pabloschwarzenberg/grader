#Ordenar tres números
numero1 = eval(input('ingresa primer número: '))
numero2 = eval(input('ingresa segundo número: '))
numero3 = eval(input('ingresa tercer número: '))

if numero1 <= numero2 <= numero3:
    print('el orden es: ', numero1 , ',' , numero2 , ',' , numero3)
if numero1 <= numero3 <= numero2:
    print('el orden es: ', numero1 , ',' , numero3 , ',' , numero2)
if numero2 <= numero1 <= numero3:
    print('el orden es: ', numero2 , ',' , numero1 , ',' , numero3)
if numero2 <= numero3 <= numero1:
    print('el orden es: ', numero2 , ',' , numero3 , ',' , numero1)
if numero3 <= numero1 <= numero2:
    print('el orden es: ', numero3 , ',' , numero1 , ',' , numero2)
if numero3 <= numero2 <= numero1:
    print('el orden es: ', numero3 , ',' , numero2 , ',' , numero1)
