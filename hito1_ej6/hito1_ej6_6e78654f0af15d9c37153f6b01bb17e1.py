x= int(input('Introducir un numero: '))
y= int(input('Introducir un numero: '))
z= int(input('Introducir un numero: '))

a= min(x, y, z)
c= max(x, y, z)
b= (x+y+z)-a-c
print ('Los numeros ordenados son: {},{},{}'.format(a, b, c))
