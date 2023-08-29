rut=input("Ingrese el rut sin digito verificador: ")
x=len(rut)
z=2
y=rut[::-1]
b=0
c=0
a=0
for i in range(x):
    b=int(y[a])*z
    c=c+b
    a=a+1
    z=z+1
    if z>7:
        z=2
print(c)
d=c%11
print(d)
e=11-d
if e>=11:
    e=0
if e==10:
    e="k"
print("dv=",e)