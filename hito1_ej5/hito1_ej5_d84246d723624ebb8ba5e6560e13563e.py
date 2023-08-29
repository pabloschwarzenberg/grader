run=input('Ingrese se RUN sin digito verificador: ')
suma=0
multiplicador=2
for rut in run [::-1]:
    suma = suma+int(rut)*multiplicador
    multiplicador= multiplicador+1
    if multiplicador >7:
        multiplicador=2
resto=suma%11
dv_temp=11-resto
if dv_temp==11:
    dv_final='0'
    print('dv='+str(dv_final))
elif dv_temp==10:
    dv_final = 'K'
    print('dv=' + str(dv_final))
else:
    dv_final=dv_temp
    print('dv='+str(dv_final))