#Cálculo del dígito verificador de un rut
r=(input('ingrese su rut:'))
rut=str(r)
if len(rut)==8:
  a=int(rut[7])*2
  b=int(rut[6:7])*3
  c=int(rut[5:6])*4
  d=int(rut[4:5])*5
  e=int(rut[3:4])*6
  f=int(rut[2:3])*7
  g=int(rut[1:2])*2
  h=int(rut[0:1])*3
if len(rut)==7:
  a=0
  b=int(rut[6])*2
  c=int(rut[5:6])*3
  d=int(rut[4:5])*4
  e=int(rut[3:4])*5
  f=int(rut[2:3])*6
  g=int(rut[1:2])*7
  h=int(rut[0:1])*2
total=a+b+c+d+e+f+g+h
div=total//11
resto=total-(11*div)
digito=11-resto
if digito==11:
  print('dv=0')
if digito==10:
  print ('dv=k')
if digito!=11 and digito!=10:
  print ('dv=',digito)