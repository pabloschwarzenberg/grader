#Cálculo del dígito verificador de un rut
r = str(input())
a = r[::-1]
if len(a)==7:
  b=int(int(a[0])*2)
  c=int(int(a[1])*3)
  d=int(int(a[2])*4)
  e=int(int(a[3])*5)
  f=int(int(a[4])*6)
  g=int(int(a[5])*7)
  h=int(int(a[6])*2)
  suma=b+c+d+e+f+g+h
  o=suma%11
  p=11-o
  if p==11:
    print("dv=0")
  elif p==10:
    print("dv=K")
  else:
    print("dv=",p) 
elif len(a)==8:
  b=int(int(a[0])*2)
  c=int(int(a[1])*3)
  d=int(int(a[2])*4)
  e=int(int(a[3])*5)
  f=int(int(a[4])*6)
  g=int(int(a[5])*7)
  h=int(int(a[6])*2)
  i = int(int(a[7])*3)
  suma=b+c+d+e+f+g+h+i
  o=suma%11
  p=11-o
  if p==11:
    print("dv=0")
  elif p==10:
    print("dv=K")
  else:
    print("dv=",p) 
