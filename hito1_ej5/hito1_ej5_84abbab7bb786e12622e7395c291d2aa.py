#Rut2
#Codigo Verificador
r=input('Ingresar el rut a verificar:')
r1=int(r)
if r1>=10000000:
    n2=r[7]
    n3=r[6]
    n4=r[5]
    n5=r[4]
    n6=r[3]
    n7=r[2]
    n8=r[1]
    n9=r[0]
    n2=int(n2)
    n3=int(n3)
    n4=int(n4)
    n5=int(n5)
    n6=int(n6)
    n7=int(n7)
    n8=int(n8)
    n9=int(n9)
          
    a=n2*2
    b=n3*3
    c=n4*4
    d=n5*5
    e=n6*6
    f=n7*7
    g=n8*2
    h=n9*3
    suma=a+b+c+d+e+f+g+h
    resultadofinal=11-suma%11
    if resultadofinal==11:
             print('dv=0')
    elif resultadofinal==10:
             print('dv=k')
    else:
                print('dv=',resultadofinal)
else:
    n2=r[6]
    n3=r[5]
    n4=r[4]
    n5=r[3]
    n6=r[2]
    n7=r[1]
    n8=r[0]
    
    n2=int(n2)
    n3=int(n3)
    n4=int(n4)
    n5=int(n5)
    n6=int(n6)
    n7=int(n7)
    n8=int(n8)
    
          
    a=n2*2
    b=n3*3
    c=n4*4
    d=n5*5
    e=n6*6
    f=n7*7
    g=n8*2
    
    suma=a+b+c+d+e+f+g
    resultadofinal=11-suma%11
    if resultadofinal==11:
             print('dv=0')
    elif resultadofinal==10:
             print('dv=k')
    else:
                print('dv=',resultadofinal)
    
