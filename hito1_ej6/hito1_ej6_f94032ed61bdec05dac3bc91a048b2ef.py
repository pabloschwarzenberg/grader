#Ordenar tres números
a = int(input('ingrese un numero'))
b = int(input('ingrese un numero'))
c = int(input('ingrese un numero'))
if a > b and a > c:
  if b < c:
    print(b,',', c,',', a)
  else:
    print(c,',', b,',', a)
if b > a and b > c:
  if a > c:
    print(c ,',',a ,',',b )
  else:
    print(a ,',',c ,',',b)
if c > a and c > b:
  if a > b:
    print(b ,',',a ,',',c )
  else:
    print(a ,',',b ,',',c)