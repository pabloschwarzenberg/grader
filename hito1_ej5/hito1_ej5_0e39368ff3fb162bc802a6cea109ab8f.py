#Cálculo del dígito verificador de un rut
n=int(input("Ingrese su rut: "))
i=2
d=0
aux=0
s=0
r=0
dv=0

while n>=1:
    aux=n%10
    if i<=7:
        d=aux*i
        s=s+d
        i=i+1
    else:
        i=2
        d=aux*i
        s=s+d
        i=i+1
    n=n//10

r=s%11
dv=11-r
if dv==10:
    print("dv= k")
elif dv==11:
    print("dv= 0")
else:
    print("dv=", dv)