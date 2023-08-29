a=int(input())
b=int(input())
c=int(input())
if a >= b:
  if b > c:
    print(a,",",b,",",c)
  if c >= b:
    if a > c:
      print(b,",",c,",",a)
    if c >= a:
      print(b,",",a,",",c)
if b > a:
  if a >= c:
    print(c,",",a,",",b)
  if c >= a:
      if b > c:
          print(a,",",c,",",b)
      if c >= b:
          print(a,",",b,",",c)