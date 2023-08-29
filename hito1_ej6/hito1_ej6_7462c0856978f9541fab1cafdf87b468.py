#Ordenar tres números
d1=int(input('ingresa un primer digito: '))
d2=int(input('ingresa un segundo digito: '))
d3=int(input('ingresa un tercer digito: '))
a=min(d1, d2, d3)
c=max(d1, d2 ,d3)
b=(d1+d2+d3)-a-c
cadena=a, b, c
print('los numeros ordenados de mayor a menor son: ',cadena)