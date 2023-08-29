a = int(input("Ingrese primer valor: "))
b = int(input("Ingrese segundo valor: "))
c = int(input("Ingrese tercer valor: "))

if (a>=c and a>=b and c>=b):
    print(b,",",c,",",a)
if (a>=c and a>=b and b>=c):
    print(c,",",b,",",a)
if (b>=a and b>=c and a>=c):
    print(c,",",a,",",b)
if (b>=a and b>=c and c>=a):
    print(a,",",c,",",b)
if (c>=a and c>=b and a>=b):
    print(b,",",a,",",c)
if (c>=a and c>=b and b>=a):
    print(a,",",b,",",c)