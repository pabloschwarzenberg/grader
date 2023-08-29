#Cálculo del dígito verificador de un rut
from math import*
rut=int(input('Ingrese su rut:'))

if len(str(rut)) == 8:
  div1 = int(str(rut)[7]) * 2
  div2=int(str(rut)[6]) * 3
  div3=int(str(rut)[5]) * 4
  div4=int(str(rut)[4]) * 5
  div5=int(str(rut)[3]) * 6
  div6=int(str(rut)[2]) * 7
  div7=int(str(rut)[1]) * 2
  div8=int(str(rut)[0]) * 3
  suma1=(div1+div2+div3+div4+div5+div6+div7+div8)
  division1=trunc((div1+div2+div3+div4+div5+div6+div7+div8)/11)
  resto1=suma1-(11*division1)
  ahora1=11-resto1

  if ahora1==11:
    print('dv=','0')
  elif ahora1==10:
    print('dv=','K')
  else:
    print('dv=',ahora1)

elif len(str(rut)) == 7:
  div1 = int(str(rut)[6]) * 2
  div2=int(str(rut)[5]) * 3
  div3=int(str(rut)[4]) * 4 
  div4=int(str(rut)[3]) * 5
  div5=int(str(rut)[2]) * 6
  div6=int(str(rut)[1]) * 7
  div7=int(str(rut)[0]) * 2
  suma2=(div1+div2+div3+div4+div5+div6+div7)
  division2=trunc((div1+div2+div3+div4+div5+div6+div7)/11)
  resto2=suma2-(11*division2)
  ahora2=11-resto2

  if ahora2==11:
    print('dv=','0')
  elif ahora2==10:
    print('dv=','K')
  else:
    print('dv=',ahora2)