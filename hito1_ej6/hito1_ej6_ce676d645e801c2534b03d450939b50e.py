print('ingrese tres numeros:')
x= eval(input('ingrese un numero:'))
y= eval(input('ingrese un numero:'))
z= eval(input('ingrese un numero:'))

if x >= y >= z:
    print('',z,',','',y,',','',x)

elif y>= x >= z:
    print('',z,',','',x,',','',y)

elif z >= x >= y:
    print('',y,',','',x,',','',z)

elif y >= z>= x:
    print('',x,',','',z,',','',y)

elif x>= z>= y:
    print('',y,',','',z,',','',x)

elif z>= y>= x:
    print('',x,',','',y,',','',z)
