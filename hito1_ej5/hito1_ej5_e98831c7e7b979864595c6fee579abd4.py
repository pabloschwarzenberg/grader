#Cálculo del dígito verificador de un rut
rut=int(input())
d1=rut%10
r1=rut//10
d2=r1%10
r2=r1//10
d3=r2%10
r3=r2//10
d4=r3%10
r4=r3//10
d5=r4%10
r5=r4//10
d6=r5%10
r6=r5//10
d7=r6%10
r7=r6//10
d8=r7%10
suma=2*d1+3*d2+4*d3+5*d4+6*d5+7*d6+2*d7+3*d8
modulo=suma%11
dv=11-modulo
if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=K")
else:
    print("dv=",dv)