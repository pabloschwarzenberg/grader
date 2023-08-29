#Descomponer un número
n=int(input())
if(n>=1000):
  x=str(n)
  z=x[:1]
  c=x[1:2]
  v=x[2:3]
  b=x[3:]
  print(z,"M +",c,"C +",v,"D +",b,"U")
elif(1000>n>=100):
  a=str(n)
  s=a[:1]
  d=a[1:2]
  f=a[2:3]
  print(s,"C +",d,"D +",f,"U")
else:
  q=str(n)
  w=q[:1]
  e=q[1:2]
  print(w,"D +",e,"U")