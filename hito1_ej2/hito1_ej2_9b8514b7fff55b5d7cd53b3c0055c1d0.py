#Contestador de celular
numero=int(input('Ingrese el numero de 8 cifras  '))
hora=int(input('Ingrese la hora de la llamada  '))
numero1=str(numero)
strnumero=str(numero)
listacompleta=[]
ultimos3=[]
primeros3=[]
for f in range(8):
    listacompleta.append(strnumero[f])
listacompleta1=listacompleta[:]
listacompleta2=listacompleta[:]
for f in range(5):
    listacompleta1.pop(0)
    ultimos3=listacompleta1
for f in range(3):
    primeros3.append(listacompleta2[f])
if hora<=7:
    print('CONTESTAR')
elif hora<14:
    if ultimos3==['9','0','9']:
        print('CONTESTAR')
    else:
        print('NO CONTESTAR')
elif hora>=17 and hora<=19:
    if primeros3==['8','7','7']:
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
elif hora>19:
    print('NO CONTESTAR')      