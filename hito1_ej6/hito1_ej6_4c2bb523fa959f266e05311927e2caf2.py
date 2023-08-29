#Ordenar tres números
a=eval(input('ingresa un numero: '))
b=eval(input('ingresa un numero: '))
c=eval(input('ingresa un numero: '))

if a<=b<=c:
    print(a,',',b,',',c)
if a<=c<=b:
    print(a,',',c,',',b)
if b<=c<=a:
    print(b,',',c,',',a)
if b<=a<=c:
    print(b,',',a,',',c)
if c<=b<=a:
    print(c,',',b,',',a)
if c<=a<=b:
    print(c,',',a,',',b)
