#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut antes del guion"))
multiplicador=2
y=int(0)
while   rut>0:
    resto=rut%10
    y=(resto*multiplicador) + y
    rut=rut//10
    multiplicador=multiplicador + 1
    if  multiplicador>7:
        multiplicador=2
w=y//11
d=y-(11*w)
s=11-d
if  s==11:
    print("dv=0")
elif    s==10:
    print("dv=k")
elif    s>=1 or s<=9:
    print("dv=",s)
