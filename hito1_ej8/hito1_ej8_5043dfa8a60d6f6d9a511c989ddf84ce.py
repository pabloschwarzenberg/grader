n=int(input())
largo=len(str(n))
if largo==4:
  u=n//1000
  n%=1000
  d=n//100
  n%=100
  t=n//10
  n%=10
  c=n
  print(u,"M +",d,"C +",t,"D +",c,"U")
if largo==3:
  d=n//100
  n%=100
  t=n//10
  n%=10
  c=n
  print(d,"C +",t,"D +",c,"U")
if largo==2:
  t=n//10
  n%=10
  c=n
  print(t,"D +",c,"U")
if largo==1:
  c=n
  print(c,"U")