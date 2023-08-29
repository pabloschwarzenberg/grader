#Cálculo del dígito verificador de un rut
rut_sin_dv=input("Ingrese el rut sin el numero siguiente al guion")
if len(rut_sin_dv)==7:
  n1=int(rut_sin_dv[6])
  n2=int(rut_sin_dv[5])
  n3=int(rut_sin_dv[4])
  n4=int(rut_sin_dv[3])
  n5=int(rut_sin_dv[2])
  n6=int(rut_sin_dv[1])
  n7=int(rut_sin_dv[0])
  a=n1*2
  b=n2*3
  c=n3*4
  d=n4*5
  e=n5*6
  f=n6*7
  g=n7*2
  suma=a+b+c+d+e+f+g
  resto=suma%11
  dv=11-resto
  if dv==11:
        print("dv=0")
  elif dv==10:
        print("dv=k")
  else:
        print("dv=",dv)

elif len(rut_sin_dv)==8:
  n1=int(rut_sin_dv[7])
  n2=int(rut_sin_dv[6])
  n3=int(rut_sin_dv[5])
  n4=int(rut_sin_dv[4])
  n5=int(rut_sin_dv[3])
  n6=int(rut_sin_dv[2])
  n7=int(rut_sin_dv[1])
  n8=int(rut_sin_dv[0])
  a=n1*2
  b=n2*3
  c=n3*4
  d=n4*5
  e=n5*6
  f=n6*7
  g=n7*2
  h=n8*3
  suma=a+b+c+d+e+f+g+h
  resto=suma%11
  dv=11-resto
  if dv==11:
        print("dv=0")
  elif dv==10:
        print("dv=K")
  else:
        print("dv=",dv)