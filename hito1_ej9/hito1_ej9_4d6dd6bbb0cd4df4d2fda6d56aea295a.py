#Sistema de Ecuaciones
a=float(input("asigne un valor para a: "))
b=float(input("asigne un valor para b: "))
c=float(input("asigne un valor para c: "))
d=float(input("asigne un valor para d: "))
e=float(input("asigne un valor para e: "))
f=float(input("asigne un valor para f: "))

formula2=(f*a-d*c)/(a*e-b*d)
formula1=(c-b*formula2)/a

if (a*e+b*d)>0:
    print("x= "+str(formula1))
    print("y= "+str(formula2))
else:
    print("ouch")     