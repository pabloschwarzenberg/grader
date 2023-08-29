#Cálculo del dígito verificador de un rut
rut=input()
largo=len(rut)

if largo==8:
  a1=int(rut[0])
  a2=int(rut[1])
  a3=int(rut[2])
  a4=int(rut[3])
  a5=int(rut[4])
  a6=int(rut[5])
  a7=int(rut[6])
  a8=int(rut[7])
  a=a8*2
  b=a7*3
  c=a6*4
  d=a5*5
  e=a4*6
  f=a3*7
  g=a2*2
  h=a1*3
  x=a+b+c+d+e+f+g+h
  y=x%11
  z=11-y
   
if largo==7:
    
  c="0"+rut
  a1=int(c[0])
  a2=int(c[1])
  a3=int(c[2])
  a4=int(c[3])
  a5=int(c[4])
  a6=int(c[5])
  a7=int(c[6])
  a8=int(c[7])
  a=a8*2
  b=a7*3
  c=a6*4
  d=a5*5
  e=a4*6
  f=a3*7
  g=a2*2
  h=a1*3
  x=a+b+c+d+e+f+g+h
  y=x%11
  z=11-y
if z==11 :
   print("dv=0")
elif z==10 :
   print("dv=k")
else :
   print("dv=",z) 