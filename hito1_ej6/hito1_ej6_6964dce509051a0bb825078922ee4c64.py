a=int(input('Ingrese su primer numero'))

b=int(input('Ingrese su segundo numero'))

c=int(input('Ingrese su tercer numero'))

if a<=b<=c:   print('El orden es: ', a, ',', b, ',', c)

if a<=c<=b:   print('El orden es: ', a, ',', c, ',', b)

if b<=a<=c:   print('El orden es: ', b, ',', a, ',', c)

if b<=c<=a:   print('El orden es: ', b, ',', c, ',', a)

if c<=a<=b:   print('El orden es: ', c, ',', a, ',', b)

if c<=b<=a:   print('El orden es: ', c, ',', b, ',', a)