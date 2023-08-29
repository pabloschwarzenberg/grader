#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese Rut: "))
d8=rut//10000000
rut=rut%10000000
d7=rut//1000000
rut=rut%1000000
d6=rut//100000
rut=rut%100000
d5=rut//10000
rut=rut%10000
d4=rut//1000
rut=rut%1000
d3=rut//100
rut=rut%100
d2=rut//10
d1=rut%10

suma=(3*d8)+(2*d7)+(7*d6)+(6*d5)+(5*d4)+(4*d3)+(3*d2)+(2*d1)
resto=suma%11
DV=11-resto

if DV==11:
    dv=0
elif DV==10:
    dv="K"
else:
    dv=DV
print("dv= ",dv)      