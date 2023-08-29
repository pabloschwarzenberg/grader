#Suma de los N primeros números
c=int(input('ingresa un numero:'))
s=int(c*(c+1)/2)
if c<=0:
    print('no es un numero natural')
if c>0:
    print('la suma es:',s)