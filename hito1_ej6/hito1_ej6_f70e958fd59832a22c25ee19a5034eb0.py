#Ordenar tres números
a=int(input("numero 1: "))
b=int(input("numero 2: "))
c=int(input("numero 3: "))
if(a>=b and a>=c):
    if(b>=c):
        print(c,b,a)
    else:
        print(b,c,a)
if(b>=a and b>=c):
    if(a>=c):
        print(c,a,b)
    else:
        print(a,c,b)
if(c>=b and c>=b):
    if(a>=b):
        print(b,a,c)
    else:
        print(a,b,c)