a=int(input())
a=str(a)
b=int(input())
b=str(b) 
c=int(input())
c=str(c)
if a<=b and b<=c:
     print(a+","+b+","+c)
elif c<=b and b<=a:
     print(c+","+b+","+a)
elif a<=c and c<=b:
     print(a+","+c+","+b)
elif b<=c and c<=a:
     print(b+","+c+","+a)
elif b<=a and a<=c:
     print(b+","+a+","+c)
elif c<=a and a<=b:
      print(c+","+a+","+b)