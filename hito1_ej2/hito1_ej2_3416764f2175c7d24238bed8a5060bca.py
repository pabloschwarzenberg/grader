t=int(input('ingrese un numero telefonico de 8 cifras:'))
h=int(input('ingrese hora de llamada:'))
if h>=0 and h<=7:
    print('contestar')
if h>7 and h<14 and t%1000==909:
    print('contestar')
if h>7 and h<14 and t%1000!=909:
    print('no contestar')
if h>=17 and h<=19 and t//100000==877:
    print('no contestar')
if h>=17 and h<=19 and t//100000!=877:
    print('contestar')
if h>19:
    print('no contestar')
