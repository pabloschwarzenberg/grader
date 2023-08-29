#Cálculo del dígito verificador de un rut
m=input("Ingrese rut sin digito verificador: ")
n=list(m)
if len(n)==8:
  pr=int(n[0])*3
  sg=int(n[1])*2
  tr=int(n[2])*7
  cr=int(n[3])*6
  qn=int(n[4])*5
  sx=int(n[5])*4
  sp=int(n[6])*3
  ov=int(n[7])*2
  numero=pr+sg+tr+cr+qn+sx+sp+ov
  resto=numero%11
  digito=11-resto
elif len(n)==7:
  pr=int(n[0])*2
  sg=int(n[1])*7
  tr=int(n[2])*6
  cr=int(n[3])*5
  qn=int(n[4])*4
  sx=int(n[5])*3
  sp=int(n[6])*2
  numero=pr+sg+tr+cr+qn+sx+sp
  resto=numero%11
  digito=11-resto
if digito==11:
  print("dv=0")
elif digito==10:
  print("dv=k")
else:
  print("dv=",digito)