#Sistema de Ecuaciones
def sistemad_de_ecuaciones(a,b,c,d,e,f):
    determinante=a*e-b*d
    if determinante !=0:
        x=(c*e-b*f)/determinante
        y=(a*f-c*d)/determinante
        print(":""["+"'""x="+str(x)+"'"+","+"y="+"'"+str(y)+"'"+"]")
        return x,y
    else:
        return None,None
print('Ingrese los valores de a, b, c, d, e y f: ')
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
e=int(input(""))
f=int(input(""))

