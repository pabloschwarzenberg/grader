#Suma de los N primeros números
n=eval(input('Indique cuantos numeros quiere sumar: '))
if n<0:
    print('Tiene que ser una cantidad mayor o igual a 0')
else:
    print('La suma de los', n, 'primeros numeros naturales es: ', (n*(n+1))/2)      