#Ordenar tres números
x1 = int(input('Escriba el primer numero: '))
x2 = int(input('Escriba el segundo numero: '))
x3 = int(input('Escriba el tercer numero: '))
a= min (x1,x2,x3)
c= max (x1,x2,x3)
b= (x1+x2+x3)-a-c
print ('Los numeros ordenados son: {}, {}, {}'.format(a,b,c))