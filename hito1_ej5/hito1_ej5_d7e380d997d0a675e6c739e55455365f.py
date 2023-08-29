#Cálculo del dígito verificador de un rut
#Cálculo del dígito verificador de un rut
r=str(input())
z=len(r)
N=r
if z==7:
    a=2*int(N[6])
    b=3*int(N[5])
    c=4*int(N[4])
    d=5*int(N[3])
    e=6*int(N[2])
    f=7*int(N[1])
    g=2*int(N[0])
    s=a+b+c+d+e+f+g
    p=s%11
    x=11-p

if z==8:
    a=2*int(N[7])
    b=3*int(N[6])
    c=4*int(N[5])
    d=5*int(N[4])
    e=6*int(N[3])
    f=7*int(N[2])
    g=2*int(N[1])
    h=3*int(N[0])
    s=a+b+c+d+e+f+g+h
    p=s%11
    x=11-p

if x==11:
    dv=0
elif x==10:
    dv="k"
else:
    dv=x
    

print("dv={}".format(dv))