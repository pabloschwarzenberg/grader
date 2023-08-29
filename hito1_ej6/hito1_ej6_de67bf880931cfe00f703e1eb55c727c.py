#Ordenar tres números
a=int(input())      
b=int(input())
c=int(input())
if c<=a and c<=b:
   if a<=b:
      print('{},{},{}'.format(c,a,b))
   if b<=a:
      print('{},{},{}'.format(c,b,a))
elif b<=a and b<=c:
    if a<=c:
       print('{},{},{}'.format(b,a,c))
    if c<=a:
       print('{},{},{}'.format(b,c,a))
elif a<=b and a<=c:
    if b<=c:
       print('{},{},{}'.format(a,b,c))
    if c<=b:
       print('{},{},{}'.format(a,c,b))
elif b<=a and b<=c:
    if a<=c:
       print('{},{},{}'.format(b,a,c))
    if c<=a:
       print('{},{},{}'.format(b,c,a))