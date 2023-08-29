a=input(print('Ingrese el valor de a'))
b=input(print('Ingrese el valor de b'))
c=input(print('Ingrese el valor de c'))

a!=b
a!=c
c!=b
if (a <= b and b <= c):

 print("{},{},{}".format(a, b, c))

if (b <= a and a <= c):

 print("{},{},{}".format(b, a, c))

if (b <= c and c <= a):

 print("{},{},{}".format(b, c, a))

if(c <= b and b <= a):

 print("{},{},{}".format(c, b, a))

if (c <= a and a <= b):

 print("{},{},{}".format(c, a, b))

if(a <= c and c <= b):

 print("{},{},{}".format(a, c, b))

