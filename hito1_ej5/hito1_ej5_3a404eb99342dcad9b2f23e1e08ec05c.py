#Cálculo del dígito verificador de un rut
a=input("ingrese su rut sin dv: ")
if len(a)==8:
  b=int(a[0])
  c=int(a[1])
  d=int(a[2])
  e=int(a[3])
  f=int(a[4])
  g=int(a[5])
  h=int(a[6])
  i=int(a[7])
  x=(i*2)+(h*3)+(g*4)+(f*5)+(e*6)+(d*7)+(c*2)+(b*3)
  x=int(x)
  y=x//11
  int(y)
  z=11-(x-(11*y))
  if z==11:
    print("dv=0")
  if z==10:
    print("dv=k")
  if z<10:
    print("dv=",z)
elif len(a)==7:
  b=int(a[0])
  c=int(a[1])
  d=int(a[2])
  e=int(a[3])
  f=int(a[4])
  g=int(a[5])
  h=int(a[6])
  x=(h*2)+(g*3)+(f*4)+(e*5)+(d*6)+(c*7)+(b*2)
  x=int(x)
  y=x//11
  int(y)
  z=11-(x-(11*y))
  if z==11:
    print("dv=0")
  if z==10:
    print("dv=k")
  if z<10:
    print("dv=",z)