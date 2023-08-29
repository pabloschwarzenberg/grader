#Sistema de Ecuaciones
x1=float(input("ingrese el valor de a: "))
y1=float(input("ingrese el valor de b: "))
z1=float(input("Ingrese el valor de c: "))
x2=float(input("Ingrese el valor de d: "))
y2=float(input("Ingrese el valor de e: "))
z2=float(input("ingrese el valor de f: "))
xaux=0
yaux=0
zaux=0
Y=0
X=0
if x1>0:
    if x2>0:
        yaux=(y1*(-x2))+(y2*x1)
        zaux=(z1*(-x2))+(z2*x1)
    else:
        yaux=(y1*x2)+(y2*x1)
        zaux=(z1*x2)+(z2*x1)
else:
    if x2<0:
        yaux=(y1*(-x2))+(y2*x1)
        zaux=(z1*(-x2))+(z2*x1)
    else:
        yaux=(y1*x2)+(y2*x1)
        zaux=(z1*x2)+(z2*x1)
if ((yaux==0) or (x1==0)):
    print("NO SE PUEDE RESOLVER")
else:
    y=zaux/yaux
    x=(z1-(y1*y))/x1
    #print("EL VALOR DE X ES: ",x ,"Y EL VALOR DE Y ES: ",y)
    print("x={}".format(round(x,1)))
    print("y={}".format(round(y,1)))