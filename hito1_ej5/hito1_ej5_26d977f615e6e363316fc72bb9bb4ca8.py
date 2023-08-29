#Cálculo del dígito verificador de un rut
rut=int(input())
run=str(rut)
if len(run)==8:
  rut0=int(run[0])*3
  rut1=int(run[1])*2
  rut2=int(run[2])*7
  rut3=int(run[3])*6
  rut4=int(run[4])*5
  rut5=int(run[5])*4
  rut6=int(run[6])*3
  rut7=int(run[7])*2
  suma=rut0 + rut1 + rut2 + rut3 + rut4 + rut5 + rut6 + rut7
  resto=suma % 11
  resultado= 11 - resto
  if resultado==11:
    print("dv=0")
  elif resultado==10:
    print("dv=k")
  else:
    print("dv=",resultado)
if len(run)==7:
  rut0=int(run[0])*2
  rut1=int(run[1])*7
  rut2=int(run[2])*6
  rut3=int(run[3])*5
  rut4=int(run[4])*4
  rut5=int(run[5])*3
  rut6=int(run[6])*2
  suma=rut0 + rut1 + rut2 + rut3 + rut4 + rut5 + rut6
  resto=suma % 11
  resultado= 11 - resto
  if resultado==11:
    print("dv=0")
  elif resultado==10:
    print("dv=k")
  else:
    print("dv=",resultado)
  