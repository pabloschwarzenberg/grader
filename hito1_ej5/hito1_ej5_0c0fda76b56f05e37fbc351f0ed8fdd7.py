#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su Rut sin digito verificador: "))
if(rut>9999999):
  ML1=((rut%100000000)//10000000)
  ML2=((rut%10000000)//1000000)
  M=((rut%1000000)//100000)
  C=((rut%100000)//10000)
  D=((rut%10000)//1000)
  U=((rut%1000)//100)
  N=((rut%100)//10)
  F=(rut%10)
  #suma de los nuemros
  run=(ML1*3+ML2*2+M*7+C*6+D*5+U*4+N*3+F*2)
  #divicion de los numeros entre 11
  div=(run//11)
  res=(run-(div*11))
  dv=(11-res)
  if(dv==11):
    print("dv=0")
  elif(dv==10):
    print("dv=k")
  else:
    print("dv=", dv)
else:
  J=((rut%10000000)//1000000)
  G=((rut%1000000)//100000)
  H=((rut%100000)//10000)
  T=((rut%10000)//1000)
  Y=((rut%1000)//100)
  O=((rut%100)//10)
  L=(rut%10)
  #suma rut de 7 dig
  run=(J*2+G*7+H*6+T*5+Y*4+O*3+L*2)
  div=(run//11)
  res=(run-(div*11))
  dv=(11-res)
  if(dv==11):
    print("dv=0")
  elif(dv==10):
    print("dv=k")
  else:
    print("dv=", dv)  