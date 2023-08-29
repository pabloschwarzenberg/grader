#Cálculo del dígito verificador de un rut
d1=0
d2=0
d3=0
d4=0
d5=0
d6=0
d7=0
d8=0
x=input("Rut: ")
if len(x)==8:
    d1=int(x[7])
    d2=int(x[6])
    d3=int(x[5])
    d4=int(x[4])
    d5=int(x[3])
    d6=int(x[2])
    d7=int(x[1])
    d8=int(x[0])
else:
    d1=int(x[6])
    d2=int(x[5])
    d3=int(x[4])
    d4=int(x[3])
    d5=int(x[2])
    d6=int(x[1])
    d7=int(x[0])
d1=d1*2
d2=d2*3
d3=d3*4
d4=d4*5
d5=d5*6
d6=d6*7
d7=d7*2
d8=d8*3
dt=d1+d2+d3+d4+d5+d6+d7+d8
rs=dt%11
vc=11-rs
dv=""
if vc<10:
    dv=str(vc)
elif vc==10:
    dv="K"
else:
    dv="0"
print("dv="+dv)
#Sale correcto pero esta raro, xke no me funciona con 7 digitos