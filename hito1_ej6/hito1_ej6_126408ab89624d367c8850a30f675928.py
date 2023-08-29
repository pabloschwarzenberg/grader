#Ordenar tres números
a=int(print())
b=int(print())
c=int(print())

if a>b>c:
print("str(c)+","+str(b)+","+str(a))
elif a>c>b:
print("str(b)+","+str(c)+","+str(a))
elif b>a>c:
print("str(c)+","+str(a)+","+str(b))
elif b>c>a:
print("str(a)+","+str(c)+","+str(b))
elif c>b>a:
print("str(a)+","+str(b)+","+str(c))
elif c>a>b:
print("str(b)+","+str(a)+","+str(c))

      