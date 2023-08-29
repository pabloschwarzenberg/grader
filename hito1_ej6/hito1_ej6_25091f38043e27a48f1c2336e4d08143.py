#Ordenar tres números
a=int(input("numero1"))
b=int(input("numero2"))
c=int(input("numero3"))
if a>=b and b>=c:
    print(str(c)+","+str(b)+","+str(a))
elif a>=b and b<=c and a>=c:
    print(str(b)+","+str(c)+","+str(a))
elif c>=a and a>=b:
    print(str(b)+","+str(a)+","+str(c))
elif c>=b and b>=a:
    print(str(a)+","+str(b)+","+str(c))
elif b>=a and a>=c:
    print(str(c)+","+str(a)+","+str(b))
elif b>=c and c>=a:
    print(str(a)+","+str(c)+","+str(b))
    