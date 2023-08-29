a=eval(input('ingrese Ingreso'))
b=eval(input('ingrese edad'))
x=eval(input('ingrese Número de hijos'))
d=eval(input('ingrese Años de pertenencia al banco'))
e=(input('ingrese Estado civil (S: soltero, C, casado) '))
f=(input('ingrese Si vive en campo o cuidad (U: urbano, R: rural)'))

if(d>10 and x>=2):
    print('APROBADO')
elif(e=='C' and x>3 and b>=1976 and b<=1966 ):
    print('APROBADO')
elif(a>2500000 and e=="S" and f=='U'):
    print('APROBADO')
elif(a>3500000 and d>5 ):
    print('APROBADO')
elif(e=='C' and x<2 and f=='R' ):
    print('APROBADO')
elif(not((d>10 and x>=2)or(e=='C' and x>3 and b>=1976 and b<=1966 )or(a>2500000 and e=="S" and f=='U')or(a>3500000 and d>5 ) or (e=='c' and x<2 and f=='R' ))):
    print('RECHAZADO')
    
