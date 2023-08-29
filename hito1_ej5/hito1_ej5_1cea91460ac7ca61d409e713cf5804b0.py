#Cálculo del dígito verificador de un rut
rut=input()
if len(rut)<8:
  rut="0"+rut
rut1=int(rut[0])*8
rut2=int(rut[1])*9
rut3=int(rut[2])*4
rut4=int(rut[3])*5
rut5=int(rut[4])*6
rut6=int(rut[5])*7
rut7=int(rut[6])*8
rut8=int(rut[7])*9
suma=rut1+rut2+rut3+rut4+rut5+rut6+rut7+rut8
resto=suma%11
if resto==10:
  print("dv=k")
else:
  print("dv="+str(resto))
  