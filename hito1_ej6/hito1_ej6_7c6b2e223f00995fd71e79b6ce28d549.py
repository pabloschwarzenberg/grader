#Ordenar tres números
print("Ingrese tres números")
a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
if a>=b and a>=c:
    if b>=c:
        print(c,",",b,",",a)
    else:
        print(b,",",c,",",a)
if b>=a and b>=c:
    if a>=c:
        print(c,",",a,",",b)
    else:
        print(a,",",c,",",b)
if c>=a and c>=b:
    if a>=b:
        print(b,",",a,",",c)
    else:
        print(a,",",b,",",c)