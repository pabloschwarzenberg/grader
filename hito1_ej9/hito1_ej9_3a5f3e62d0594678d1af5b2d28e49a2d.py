#Sistema de Ecuaciones
x1=int(input())
y1=int(input())
r1=int(input())
x2=int(input())
y2=int(input())
r2=int(input())
if x1==x2:
  if y2-y1>=0:
    a=(r2-r1)/(y2-y1)
    b=(r1-y1*a)/x1
    print("x=",a)
    print("y=",b)
  if y2-y1<=0:
    a=(r1-r2)/(y1-y2)
    b=(r1-y1*a)/x1
    print("x=",a)
    print("y=",b)
if y1==y2:
  if x2-x1>=0:
    a=(r2-r1)/(x2-x1)
    b=(r1-x1*a)/y1
    print("x=",a)
    print("y=",b)
  if x2-x1<=0:
    a=(r1-r2)/(x1-x2)
    b=(r1-x1*a)/y1
    print("x=",a)
    print("y=",b)
if x1!=x2 and y1!=y2:
    if x1>0 and x2>0:
      a=(r2*x1-r1*x2)/(x1*y2-x2*y1)
      b=(r1-a*y1)/x1
      print("x=",b)
      print("y=",a)
    elif x1<0 or x2<0:
      a=(r2*x1+r1*x2)/(x1*y2+x2*y1)
      b=(r1-a*y1)/x1
      print("x=",a)
      print("y=",b)