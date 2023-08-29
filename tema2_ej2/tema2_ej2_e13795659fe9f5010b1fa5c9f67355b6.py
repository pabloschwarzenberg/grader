#2 puntos
import os
os.system('cls')

#Funcion si es amigo
def amigos(numero1, numero2):
    sum_numero1 = 0
    sum_numero2 = 0

    if (numero1 == numero2) :
       return False

    for divisor in range(1, numero1+1):
        if (numero1 % divisor) == 0 :
            sum_numero1 += divisor

    for divisor in range(1, numero2+1):
        if (numero2 % divisor) == 0 :
            sum_numero2 += divisor
    if (sum_numero1 == sum_numero2) :
        return True
    else :
        return False

#Numero 1
numero1 = 0
try:
    numero1 = int(input('Ingrese el numero 1 numero:'))
except:
    print('Error : Debe ingresar un numero entero')

#Numero 2
numero2 = 0
try:
    numero2 = int(input('Ingrese el numero 2 numero:'))
except:
    print('Error : Debe ingresar un numero entero')

res = amigos(numero1, numero2)
print(res)