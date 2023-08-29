#Sistema de Ecuaciones
def sistemaEcuaciones(a,b,c,d,e,f):
    determinador=a*e-b*d
    if determinador !=0:
        x=((c*e-b*f)/determinador)
        y=((a*f-c*d)/determinador)
        print('x=',x,'\ny=',y,sep='')
    else:
        return  None, None

a=int(input("Ingrese un numero:\n "))
b=int(input("Ingrese un numero:\n "))
c=int(input("Ingrese un numero:\n "))
d=int(input("Ingrese un numero:\n "))
e=int(input("Ingrese un numero:\n "))
f=int(input("Ingrese un numero:\n "))

sistemaEcuaciones(a,b,c,d,e,f)