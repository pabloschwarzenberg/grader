#Ordenar tres números
a=int(input('ingresa un numero:'))
b=int(input('ingresa un numero:'))
c=int(input('ingresa un numero:'))
if a>=b>=c:
    print('el orden es:', c,',', b,',', a)
if b>=a>=c:
    print('el orden es:', c,',', a,',', b)
if c>=a>=b:
    print('el orden es:', b,',', a,',', c)
if a>=c>=b:
    print('el orden es:', b,',', c,',', a)
if b>=c>=a:
    print('el orden es:', a,',', c,',', b)
if c>=b>=a:
    print('el orden es:', a,',', b,',', c)
