#Cálculo del dígito verificador de un rut
rut=int(input('Ingrese RUT sin verificador ni puntos: '))

n1= rut%10
rut=rut//10

n2= rut%10
rut=rut//10

n3= rut%10
rut=rut//10

n4= rut%10
rut=rut//10

n5= rut%10
rut=rut//10

n6= rut%10
rut=rut//10

n7= rut%10
rut=rut//10

n8= rut%10
rut=rut//10

suma=n1*2 + n2*3 + n3*4 + n4*5 + n5*6 + n6*7 + n7*2 + n8*3 
resto=suma%11
resultado=11-resto

if resultado==11:
    dv=0
else:
    if resultado==10:
        dv='K'
    else:
        dv=resultado

print('dv=',dv)

