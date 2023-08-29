rut = int(input("Ingrese su rut , si tiene menos de ocho digito comienze con 0:  "))
rut1=str(rut)
rut2=len(rut1)
if rut2==8:
  x = rut//10
  x1 = rut%10

  y = x//10
  y1 = x%10

  z = y//10
  z1 = y%10

  a = z//10
  a1 = z%10

  b = a//10
  b1 = a%10

  c = b//10
  c1 = b%10

  d = c//10
  d1 = c%10

  e = d//10
  e1 = d%10

  suma_digitos = (x1*2) + (y1*3) + (z1*4) + (a1*5) + (b1*6) + (c1*7) + (d1*2) + (e1*3)

  resto = suma_digitos%11

  verificador = 11 - resto

  if verificador == 10:
    verificador="k"
    print("dv=",verificador)

  else:
    print("dv=",verificador)
if rut2==7:

  digito7=rut%10
  
  digito6=(rut//10)
  digito6=(digito6%10)
  
  digito5=(rut//100)
  digito5=(digito5%10)
  
  digito4=(rut//1000)
  digito4=(digito4%10)
  
  digito3=(rut//10000)
  digito3=(digito3%10)
  
  digito2=(rut//100000)
  digito2=(digito2%10)
  
  digito1=(rut//1000000)
  digito1=(digito1%10)
  
  suma_digitos=(digito7*2)+(digito6*3)+(digito5*4)+(digito4*5)+(digito3*6)+(digito2*7)+(digito1*2)
  
  resto = suma_digitos%11
  if resto==0:
    verificador=0
    print("dv=",verificador)
  else:
    verificador = 11 - resto

    if verificador == 10:
      verificador="k"
      print("dv=",verificador)

    else:
      print("dv=",verificador)