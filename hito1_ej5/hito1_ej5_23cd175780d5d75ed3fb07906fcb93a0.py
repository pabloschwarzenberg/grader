#Cálculo del dígito verificador de un rut
rut=int(input(" Ingrese el rut para calcular el digito verifícador: "))

dM=rut//10000000
r1=rut%10000000
uM=r1//1000000
r2=r1%1000000
cm=r2//100000
r3=r2%100000
dm=r3//10000
r4=r3%10000
um=r4//1000
r5=r4%1000
c=r5//100
r6=r5%100
d=r6//10
u=rut%10

suma=u*2+d*3+c*4+um*5+dm*6+cm*7+uM*2+dM*3
resto=suma%11
verificador=11-resto
if verificador==11:
    print("dv=",0)
elif verificador==10:
    print("dv=",'k')
else:
    print("dv=",verificador)

