a=int(input("Escriba el primer número"))
b=int(input("Escriba el segundo número"))
c=int(input("Escriba el tercer número"))

d=c,b,a
e=b,c,a
f=a,c,b
g=c,a,b
h=b,a,c
i=a,b,c

if a>=b>=c:
    print(list(d))
    
if a>=c>=b:
    print(list(e))
    
if b>=c>=a:
    print(list(f))
    
if b>=a>=c:
    print(list(g))


if c>=a>=b:
    print(list(h))
    
if c>=b>=a:
    print(list(i))
      