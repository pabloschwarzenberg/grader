#Contestador de celular
import random
print()
print()
print('%%%%%%%% Bienvenido a CONTESTAR %%%%%%%%%')
print()
print()

num= int(input('Ingrese numero telefonico: '))
a=len(str(num))
b=num%1000
c=num//10000
if a!=8:
    print('Error, el numero ingresado no existe')
h=int(input('Ingrese hora de la llamada: '))
if h>=0 and h<=7:
    print('Resultado: CONTESTAR')
if h>7 and h<14:
        if b!=909:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')
if h>=17 and h<=19:
        if c!=877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')
if h>19 and h<=24:
    print('Resultado: NO CONTESTAR')
        
