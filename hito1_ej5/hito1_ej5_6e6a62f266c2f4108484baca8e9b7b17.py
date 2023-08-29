#Cálculo del dígito verificador de un rut
n1=int(input("ingresa tu rut: ")) 
rut=str(n1)
x=len(rut)
l1=rut[0:1]
l2=rut[1:2]
l3=rut[2:3]
l4=rut[3:4]
l5=rut[4:5]
l6=rut[5:6]
l7=rut[6:7]
l8=rut[7:8]


if(x == 7):
  f1 =int(l1*1)*2
  f2 =int(l2*1)*7
  f3 =int(l3*1)*6
  f4 =int(l4*1)*5
  f5 =int(l5*1)*4
  f6 =int(l6*1)*3
  f7 =int(l7*1)*2
  adicion=(f1+f2+f3+f4+f5+f6+f7)
  modulo= (adicion // 11)
  resto = adicion-( 11 * modulo)
  resultado = (11 - resto)
  if(resultado == 11):
    print("dv=0")
  elif(resultado == 10):
    print("dv=K")
  else:
    print("dv=", resultado)
elif(x == 8):
  f1 =int(l1*1)*3
  f2 =int(l2*1)*2
  f3 =int(l3*1)*7
  f4 =int(l4*1)*6
  f5 =int(l5*1)*5
  f6 =int(l6*1)*4
  f7 =int(l7*1)*3
  f8 =int(l8*1)*2
  adicion=(f1+f2+f3+f4+f5+f6+f7+f8)
  modulo= (adicion // 11)
  resto = adicion-( 11 * modulo)
  resultado = (11 - resto)
  if(resultado == 11):
    print("dv=0")
  elif(resultado == 10):
    print("dv=k")
  else:
    print("dv=", resultado)