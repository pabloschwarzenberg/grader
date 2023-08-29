#Cálculo del dígito verificador de un rut
numero=int(input('Escoje tu rut: '))
Pr=int(numero/10000000)
Seg=int((numero%10000000)/1000000)
Ter=int((numero%1000000)/100000)
Cua=int((numero%100000)/10000)
Quin=int((numero%10000)/1000)
Sex=int((numero%1000)/100)
Sep=int((numero%100)/10)
Oct=numero%10
S=Pr*3+Seg*2+Ter*7+Cua*6+Quin*5+Sex*4+Sep*3+Oct*2
D=S%11
dv=11-D
if dv==10:
    print('dv=k')
elif dv==11:
    print('dv=',0)
else:
    print('dv=',dv)