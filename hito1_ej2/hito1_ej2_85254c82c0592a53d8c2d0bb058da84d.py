#Contestador de celular
n=eval(input('Ingrese número teléfonico de 8 cifras:'))
h=eval(input('Ingrese hora de llamada:'))
if 0<=h<=7:
    print('Contestar')
if 7<h<14 and n%1000==909:
    print('Contestar')
if 7<h<14 and not n%1000==909:
        print('No Contestar')
if 14<=h<17:
    print('No Contestar')
if 17<=h<=19 and not n//100000==877:
    print('Contestar')
if 17<=h<=19 and n//100000==877:
     print('No Contestar')
if h>19:
    print('No Contestar')
      