#Aprobación de créditos
a=input('cual es su ingreso actual:')
b=input('en que año nacio :')
c=input('cuantos hijos tiene :')
d=input('cuanto tiempo lleva en el banco:')
e=input('cual es su estado civil:')
f=input('vive en el campo o en la ciudad :')
a=int(a)
b=int(b)
c=int(c)
d=int(d)
anos=2017-b
if d>10 and c>=2:
    print('APROBADO')
elif e =='C' and c>3 and anos<=55 and anos>=45:
    print('APROBADO')
elif a>2500000 and e == 'S' and f=='U':
    print('APROBADO')
elif a>3500000 and d>5:
    print('APROBADO')
elif c<2 and f=='R' and e== 'C':
    print('APROBADO')
else :
    print('RECHAZADO')