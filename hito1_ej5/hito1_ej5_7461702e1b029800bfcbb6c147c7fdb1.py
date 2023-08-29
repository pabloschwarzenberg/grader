#Cálculo del dígito verificador de un rut
rut=int(input('ingrese su rut, sin puntos ni guiones: '))
A=rut%10
MA=A*2
rut=rut//10

B=rut%10
MB=B*3
rut=rut//10

C=rut%10
MC=C*4
rut=rut//10

D=rut%10
MD=D*5
rut=rut//10

E=rut%10
ME=E*6
rut=rut//10

F=rut%10
MF=F*7
rut=rut//10

G=rut%10
MG=G*2
rut=rut//10

H=rut%10
MH=H*3

suma=MA+MB+MC+MD+ME+MF+MG+MH
promedio=suma//11
resto=suma-(11*promedio)
final=11-resto

if final==11:
    dv=0
    print('dv=',dv)
else:
    if final==10:
        dv='k'
        print('dv=',dv)
    else:
        dv=final
        print('dv=',dv)