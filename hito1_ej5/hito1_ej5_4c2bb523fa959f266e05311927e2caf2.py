#Cálculo del dígito verificador de un rut
rut=int(input('ingrese rut sin puntos ni digito verificador: '))
DV1=(rut%10)
rut=rut//10
DV2=(rut%10)
rut=rut//10
DV3=(rut%10)
rut=rut//10
DV4=(rut%10)
rut=rut//10
DV5=(rut%10)
rut=rut//10
DV6=(rut%10)
rut=rut//10
DV7=(rut%10)
rut=rut//10
DV8=(rut%10) 

suma=(DV1*2 + DV2*3 + DV3*4 + DV4*5 + DV5*6 + DV6*7 + DV7*2 + DV8*3)%11
digito=11-suma

if digito==10:
    print('dv=k')
elif digito==11:
    print('dv=0')
else:
    print('dv=',digito)