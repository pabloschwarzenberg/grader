#Sistema de Ecuaciones
def sistema_ec(a,b,c,d,e,f):
    determinante= a*e - b*d
    if determinante != 0 :
        x=(c*e - b*f)/determinante
        y=(a*f - c*d)/determinante
        print('x=',x,'y=',y)
    else:
        return None, None
a= float(input('Variable 1: '))
b= float(input('Variable 2: '))
c= float(input('Variable 3: '))
d= float(input('Variable 4: '))
e= float(input('Variable 5: '))
f= float(input('Variable 6: '))
print(sistema_ec(a,b,c,d,e,f))     