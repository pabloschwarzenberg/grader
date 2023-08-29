#Cálculo del dígito verificador de un rut
rut=input("rut")
rut=rut[::-1]
if len(rut)==8:
  numero1=int(rut[0])*2+int(rut[1])*3+int(rut[2])*4+int(rut[3])*5+int(rut[4])*6+int(rut[5])*7+int(rut[6])*2+int(rut[7])*3
  dv=11-numero1%11
if len(rut)==7:
  numero1=int(rut[0])*2+int(rut[1])*3+int(rut[2])*4+int(rut[3])*5+int(rut[4])*6+int(rut[5])*7+int(rut[6])*2
  dv=11-numero1%11
if dv==11:
  dv=0
  print("dv=",dv)
elif dv==10:
  dv="k"
  print("dv=", dv)
else:
  print("dv=", dv)
  