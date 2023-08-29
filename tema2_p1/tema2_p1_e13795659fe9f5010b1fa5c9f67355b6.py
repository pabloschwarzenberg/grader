#2 puntos
import os
os.system('cls')

#Funcion si es primo
def es_primo(num):
    if (num == 1) :
       return False 
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

#Numero
numero = 0
try:
    #Funcion input para leer el numero de intentos
    numero = int(input('Ingrese un numero:'))
except:
    print('Error : Debe ingresar un numero entero')

#Calulamos si es primo
primo = ''
primo = es_primo(numero)

#Print
print(primo)