a=int(input())
b=int(input())
c=int(input())
if (a<=b<=c):
  print (a,",",b,",", c)
if (a>=b>=c):
  print (c,",",b,",", a)
if (c<=a<=b):
  print (c,",",a,",", b)
if (b<=a<=c):
  print (b,",",a,",", c)
if (b<=c<=a):
  print (b,",",c,",", a)
if (a<=c<=b):
  print (a,",",c,",", b)