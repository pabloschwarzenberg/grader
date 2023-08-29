#Cálculo del dígito verificador de un rut
rut=input("Ingrese su rut: ")
rut_inv=""
for a in rut:
  rut_inv= a + rut_inv
if len(rut)==8:
  a=int(rut_inv[0])*2
  b=int(rut_inv[1])*3
  c=int(rut_inv[2])*4
  d=int(rut_inv[3])*5
  e=int(rut_inv[4])*6
  f=int(rut_inv[5])*7
  g=int(rut_inv[6])*2
  h=int(rut_inv[7])*3
  suma= a+b+c+d+e+f+g+h
elif len(rut)==7:
  a=int(rut_inv[0])*2
  b=int(rut_inv[1])*3
  c=int(rut_inv[2])*4
  d=int(rut_inv[3])*5
  e=int(rut_inv[4])*6
  f=int(rut_inv[5])*7
  g=int(rut_inv[6])*2
  suma= a+b+c+d+e+f+g

resto= suma%11
dv=11-resto
if dv==10:
  print("dv= K")
elif dv==11:
  print("dv= 0")
else:
 print("dv= ",dv)