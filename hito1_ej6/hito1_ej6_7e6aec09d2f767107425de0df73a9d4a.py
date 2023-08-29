#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
a=str(a)
b=str(b)
c=str(c)
if a<=b and b<=c:
     print(a+","+b+","+c)
elif a<=c and c<=b:
     print(a+","+c+","+a)
elif b<=c and c<=a:
     print(b+","+c+","+a)
elif b<=a and a<=c:
     print(b+","+a+","+c)
elif c<=b and b<=a:
     print(c+","+b+","+a)
elif c<=a and a<=b:
     print(c+","+a+","+b)