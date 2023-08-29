#Juego adivina mi número
##import##
from random import *

##variable##
Intentos=5

##main##
M_Num=randrange(1,21)

num_us=0
while (num_us!=M_Num) or (Intentos>0):
    num_us=int(input('¿Cúal sera mi número?'))
    if num_us>M_Num:
        print('Mi número es menor')
        Intentos=Intentos-1
    if num_us<M_Num:
        print('Mi número es mayor')
        Intentos=Intentos-1
    if Intentos==0:
        break
    if num_us==M_Num:
        break
if Intentos==0:
    print('No adivinaste, mi número era:',M_Num)
if num_us==M_Num:
    print('Adivinaste, mi número era:',num_us)