import random

valor = random.randint(1, 20)
vuelta = 0
numero = 0

print('Adivina el valor incognito entre 1 y 20')

while numero != valor:
    vuelta += 1
    numero = input('Ingresa un numero #{}: '.format(vuelta))
    
    if numero.isnumeric():
        numero = int(numero)
    else:
        print('Porfavor solo ingresar numeros')
        continue
           
    if numero > valor:
            print('El valor ingresado es muy alto, intentalo nuevamente!')
    
    if numero < valor:
            print('El numero ingresado es muy bajo, intentalo nuevamente!')

else:
    print('lo adivinaste en {} intentos'.format(vuelta))

