#Cálculo del dígito verificador de un rut
rut=int(input())
if(rut<10000000):
  rup=str(rut)
  r0=rup[:1]
  r1=rup[1:2]
  r2=rup[2:3]
  r3=rup[3:4]
  r4=rup[4:5]
  r5=rup[5:6]
  r6=rup[6:7]
  w0=int(r0)
  w1=int(r1)
  w2=int(r2)
  w3=int(r3)
  w4=int(r4)
  w5=int(r5)
  w6=int(r6)
  l=(w0*2)
  k=(w1*7)
  j=(w2*6)
  h=(w3*5)
  g=(w4*4)
  f=(w5*3)
  d=(w6*2)
  suma=(l+k+j+h+g+f+d)
  resto=(suma%11)
  tr=(11-resto)
  if(tr==10):
    print("dv=k")
  elif(tr==11):
    print("dv=0")
  else:
    print("dv=",tr)
else:
  ruk=str(rut)
  a0=ruk[:1]
  a1=ruk[1:2]
  a2=ruk[2:3]
  a3=ruk[3:4]
  a4=ruk[4:5]
  a5=ruk[5:6]
  a6=ruk[6:7]
  a7=ruk[7:]
  e0=int(a0)
  e1=int(a1)
  e2=int(a2)
  e3=int(a3)
  e4=int(a4)
  e5=int(a5)
  e6=int(a6)
  e7=int(a7)
  m=(e0*3)
  n=(e1*2)
  b=(e2*7)
  v=(e3*6)
  c=(e4*5)
  x=(e5*4)
  z=(e6*3)
  q=(e7*2)
  total=(m+n+b+v+c+x+z+q)
  res=(total%11)
  yu=(11-res)
  if(yu==10):
    print("dv=k")
  else:
    print("dv=",yu)
  
  
  


  