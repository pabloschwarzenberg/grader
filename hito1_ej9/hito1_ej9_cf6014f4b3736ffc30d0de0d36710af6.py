x=int(input('ingresar x'))
y=int(input('ingresar y'))

sol=int(input('ingresar solucion'))
x1=int(input('ingresar x2'))
y1=int(input('ingresar y2'))

sol1=int(input('ingresar solucion 2'))

EKIS= ((sol*y1)-(y*sol1))
EKISDE= ((x*y1)-(y*x1))
LINDA=  str(float(EKIS//EKISDE))

YKEPAZA= ((x*sol1)-(sol*x1))
LINDO= str(float(YKEPAZA//EKISDE))

print('x='+ LINDA)
print('y='+ LINDO)
      