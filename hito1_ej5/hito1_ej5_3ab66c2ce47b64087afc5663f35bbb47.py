#Cálculo del dígito verificador de un rut
n=int(input("Ingrese su rut: "))
a=2
b=0
c=0
d=0
e=0
dv=0

while n>=1:
    c=n%10
    if a<=7:
        b=c*a
        d=d+b
        a=a+1
    else:
        a=2
        b=c*a
        d=d+b
        a=a+1
    n=n//10

e=d%11
dv=11-e
if dv==10:
    print("dv= k")
elif dv==11:
    print("dv= 0")
else:
    print("dv=", dv)
