#Ordenar tres números
a=eval(input('Escribe el primer numero: '))
b=eval(input('Escribe el segundo numero: '))
c=eval(input('Escribe el tercer numero: '))
if a<b and a<c and b<c:
    print('Los numeros de menor a mayor son: ', a, ',', b, ',', c)
elif a<b and a<c and c<b:
    print('Los numeros de menor a mayor son: ', a, ',', c, ',', b)
elif b<a and b<c and a<c:
    print('Los numeros de menor a mayor son: ', b, ',', a, ',', c)
elif b<a and b<c and c<a:
    print('Los numeros de menor a mayor son: ', b, ',', c, ',', a)
elif c<a and c<b and a<b:
    print('Los numeros de menor a mayor son: ', c, ',', a, ',', b)
elif c<a and c<b and b<a:
    print('Los numeros de menor a mayor son: ', c, ',', b, ',', a)
elif a<b and a<c and b==c:
    print('Los numeros de menor a mayor son: ', a, ',', b, ',', c)
elif a>b and a>c and c==b:
    print('Los numeros de menor a mayor son: ', b, ',', c, ',', a)
elif b<a and b<c and a==c:
    print('Los numeros de menor a mayor son: ', b, ',', c, ',', a)
elif b>a and b>c and a==c:
    print('Los numeros de menor a mayor son: ', a, ',', c, ',', b)
elif c<a and c<b and a==b:
    print('Los numeros de menor a mayor son: ', c, ',', a, ',', b)
elif c>a and c>b and a==b:
    print('Los numeros de menor a mayor son: ', a, ',', c, ',', b)
elif a==b==c:
    print('Todos los numeros son iguales: ', a, ',', c, ',', b)