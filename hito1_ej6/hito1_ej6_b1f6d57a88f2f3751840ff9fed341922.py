
a=int(input())
b=int(input())
c=int(input())
if a<=b<=c:
  print("{},{},{}".format(a,b,c))
if a<=c<=b:
  print("{},{},{}".format(a,c,b))
if b<=c<=a:
  print("{},{},{}".format(b,c,a))
if b<=a<=c:
  print("{},{},{}".format(b,a,c))
if c<=b<=a:
  print("{},{},{}".format(c,b,a))
if c<=a<=b:
  print("{},{},{}".format(c,a,b))