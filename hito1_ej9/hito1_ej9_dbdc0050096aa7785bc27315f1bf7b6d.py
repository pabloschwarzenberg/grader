#Sistema de Ecuaciones

a = eval(input('Ingresar primer numero: '))
b = eval(input('Ingresar segunado numero: '))
c = eval(input('Ingresar tercero numero: '))
d = eval(input('Ingresar cuarto numero: '))
e = eval(input('Ingresar quinto numero: '))
f = eval(input('Ingresar sexto numero: '))

#print(a,'x +',b,'y =',c)
#print(d,'x +',e,'y =',f)

determinante = (a*e)-(d*b)
print('x =',((c*e)-(f*b))/determinante)
print('y =',((a*f)-(d*c))/determinante)      