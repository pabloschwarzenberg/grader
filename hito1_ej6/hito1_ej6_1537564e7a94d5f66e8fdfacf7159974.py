a=int(input("Escriba el primer número:"))
b=int(input("Escriba el segundo número:"))
c=int(input("Escriba el tercero número:"))

d=a,b,c
e=a,c,b
f=b,a,c
g=b,c,a
h=c,a,b
i=c,b,a


if a>=b>=c:
    print(i)
elif a>=c>=b:
    print(g)
elif b>=a>=c:
    print(h)
elif b>=c>=a:
    print(e)
elif c>=a>=b:
    print(f)
elif c>=b>=a:
    print(d)
      