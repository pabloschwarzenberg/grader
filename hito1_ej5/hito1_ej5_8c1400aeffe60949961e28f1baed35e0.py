#Cálculo del dígito verificador de un rut
a=int(input("ingrese rut sin dv:"))
b=a//10000000
c=a//1000000-10*b
d=a//100000-100*b-10*c
e=a//10000-1000*b-100*c-10*d
f=a//1000-10000*b-1000*c-100*d-10*e
g=a//100-100000*b-10000*c-1000*d-100*e-10*f
h=a//10-1000000*b-100000*c-10000*d-1000*e-100*f-10*g
i=a-10000000*b-1000000*c-100000*d-10000*e-1000*f-100*g-10*h
x=b*3+c*2+d*7+e*6+f*5+g*4+h*3+i*2
z=x%11
dv=11-z
if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=K")
else:
    print("dv=", dv)     