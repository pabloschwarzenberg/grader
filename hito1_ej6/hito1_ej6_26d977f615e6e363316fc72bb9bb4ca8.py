a=int(input())
b=int(input())
c=int(input())
if a>=b and b>=c:
  print(c,",",b,",",a)
if b>=a and a>=c: 
  print(c,",",a,",",b)
if c>=a and a>=b:
  print(b,",",a,",",c)
if a>=c and c>=b:
  print(b,",",c,",",a)
if c>=b and b>=a:
  print(a,",",b,",",c)
if b>=c and c>=a:
  print(a,",",c,",",b)