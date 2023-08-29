#Ordenar tres números
a=int(input("Dame un numero"))
b=int(input("Dame un numero"))
c=int(input("Dame un numero"))
if a>b and b>c:
   print(c,b,a)
elif a>b and b<c and a>c:
   print(b,c,a)
elif b>a and a>c:
   print(c,a,b)
elif b>a and c>a and b>c:
   print(a,c,b)
elif c>a and a>b:
   print(b,a,c)
else:
   print(a,b,c)