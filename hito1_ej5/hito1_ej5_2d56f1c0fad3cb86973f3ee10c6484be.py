#Cálculo del dígito verificador de un rut
RUT=(input())
if len(RUT)==7:
  n1=int(RUT[6])
  n2=int(RUT[5])
  n3=int(RUT[4])
  n4=int(RUT[3])
  n5=int(RUT[2])
  n6=int(RUT[1])
  n7=int(RUT[0])
  a=n1*2
  b=n2*3
  c=n3*4
  d=n4*5
  e=n5*6
  f=n6*7
  g=n7*2
  s=a+b+c+d+e+f+g
  r=s%11
  dv=11-r
  if dv==11:
    print("dv=0")
  elif dv==10:
    print ("dv=k")
  else:
    print("dv=",dv)
elif len(RUT)==8:
  n1=int(RUT[7])
  n2=int(RUT[6])
  n3=int(RUT[5])
  n4=int(RUT[4])
  n5=int(RUT[3])
  n6=int(RUT[2])
  n7=int(RUT[1])
  n8=int(RUT[0])
  a=n1*2
  b=n2*3
  c=n3*4
  d=n4*5
  e=n5*6
  f=n6*7
  g=n7*2
  h=n8*3
  s=a+b+c+d+e+f+g+h
  r=s%11
  dv=11-r
  if dv==11:
    print("dv=0")
  elif dv==10:
    print ("dv=k")
  else:
    print("dv=",dv)  
