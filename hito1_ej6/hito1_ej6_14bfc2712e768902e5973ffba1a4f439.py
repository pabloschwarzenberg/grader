#Ordenar tres números
print('ingrese 3 numeros')
a=int(input(''))
b=int(input(''))
c=int(input(''))
minimo=min(a, b, c)
maximo=max(a, b, c)
el_del_medio=(a+b+c)-minimo-maximo
print(minimo,',',el_del_medio,',',maximo)
