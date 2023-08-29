#Ordenar tres números
a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))
c=int(input("Ingrese un último número: "))
if a>=b and b>=c: 
 print(c,",", b,",", a)
elif b>=a and a>=c:
 print(c,",", a,",", b)
elif c>=a and a>=b:
 print(b,",", a,",", c)
elif b>=c and c>=a: 
 print(a,",", c,",", b)
elif c>=b and b>=a:
 print(a,",", b,",", c)
else:
 print(b,",", c,",", a)