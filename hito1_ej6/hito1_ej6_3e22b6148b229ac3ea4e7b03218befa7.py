#Ordenar tres números
x = int(input('ingresa  un numero x :'))
y = int(input('ingresa  un numero y :'))
z = int(input('ingresa  un numero z :'))

if z<=y<=x:
    print ('Los tres numeros ordenados de menor a mayor son', z, ',', y , ',', x )
elif z<=x<=y:
    print ('Los tres numeros ordenados de menor a mayor son', z, ',', x , ',', y )
elif y<=z<=x:
    print ('Los tres numeros ordenados de menor a mayor son', y, ',', z , ',', x)
elif y<=x<=z:
    print ('Los tres numeros ordenados de menor a mayor son', y, ',', x , ',', z)
elif x<=z<=y:
    print ('Los tres numeros ordenados de menor a mayor son', x, ',', z , ',', y)
elif x<=y<=z:
    print ('Los tres numeros ordenados de menor a mayor son', x, ',', y , ',', z)
