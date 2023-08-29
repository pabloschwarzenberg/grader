rut=str(input())
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
suma=0
resultado=0
if len(rut)==7:
  a=int(rut[6])*2
  b=int(rut[5])*3
  c=int(rut[4])*4
  d=int(rut[3])*5
  e=int(rut[2])*6
  f=int(rut[1])*7
  g=int(rut[0])*2
  suma= a+b+c+d+e+f+g
  resultado= suma%11
  dv= 11-resultado
  if dv==11:
    print("dv=0")
  elif dv==10:
    print("dv=k")
  else:
    print("dv=",dv)
elif len(rut)==8:
   h=int(rut[7])*2
   a=int(rut[6])*3
   b=int(rut[5])*4
   c=int(rut[4])*5
   d=int(rut[3])*6
   e=int(rut[2])*7
   f=int(rut[1])*2
   g=int(rut[0])*3
   suma= a+b+c+d+e+f+g+h
   resultado= suma%11
   dv= 11-resultado
   if dv==11:
    print("dv=0")
   elif dv==10:
    print("dv=k")
   else:
    print("dv=",dv)
elif len(rut)==9:
  a=int(rut[8])*2
  b=int(rut[7])*3
  c=int(rut[6])*4
  d=int(rut[5])*5
  e=int(rut[4])*6
  f=int(rut[3])*7
  g=int(rut[2])*2
  h=int(rut[1])*3
  i=int(rut[0])*4
  suma=a+b+c+d+e+f+g+h+i
  resultado=suma%11
  dv= 11-resultado
  if dv==11:
    print("dv=0")
  elif dv==10:
    print("dv=k")
  else:
    print("dv=",dv)
else:
  print("rut no valido")