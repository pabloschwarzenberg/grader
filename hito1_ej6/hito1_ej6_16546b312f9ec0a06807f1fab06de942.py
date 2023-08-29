#Ordenar tres números
a=input("ingrese un numero: ")
b=input("ingrese el segundo numero: ")
c=input("ingrese el tercer numero: ")
if(a<=b<=c):
 print(a, b, c)
if(b<=a<=c):
 print(b, a, c)
if (c<=b<=a):
 print(c, b, a)
if(a<=c<=b):
 print(a,",", c,",", b)
if(b<=c<=a):
 print(b, ",", c,",", a)
if(c<=a<=b):
 print(c, ",", a,",", b)