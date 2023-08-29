#Cálculo del dígito verificador de un rut
#anibal muñoz
x=str(input(print("ingrse su rut y le daremos su codigo verificador")))
if(len(x)==8):
    a=2*int(x[7])
    s=3*int(x[6])
    d=4*int(x[5])
    f=5*int(x[4])
    g=6*int(x[3])
    h=7*int(x[2])
    j=2*int(x[1])
    k=3*int(x[0])
    l=int(a)+int(s)+int(d)+int(f)+int(g)+int(h)+int(j)+int(k)
    ñ=int(l)//11
    z=int(l)-(11*ñ)
    y=11-z
    if(y==11):
        print("dv=0")
    elif(y==10):
        print("dv=k")
    else:
        print("dv=",y)

if(len(x)==7):
    a=2*int(x[6])
    s=3*int(x[5])
    d=4*int(x[4])
    f=5*int(x[3])
    g=6*int(x[2])
    h=7*int(x[1])
    j=2*int(x[0])
    l=int(a)+int(s)+int(d)+int(f)+int(g)+int(h)+int(j)
    ñ=int(l)//11
    z=int(l)-(11*ñ)
    y=11-z
    if(y==11):
        print("dv=0")
    elif(y==10):
        print("dv=k")
    else:
        print("dv=",y)