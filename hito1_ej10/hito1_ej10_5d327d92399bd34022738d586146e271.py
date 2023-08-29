while True:
  
  print("Bienbenido")
  saldo=1000000
  print("saldo cajero $",saldo)
  u=int(input("ingrese el nº de usuario:"))
  sc=100000
  s= chr(49)+chr(56)+chr(48)+chr(51) 
  i=0
  while i < 3 :
    clave=input("Por favor ingrese la clave: ")
    if clave==s and u==10334151:
      c=1
      print("clave valida")
      break
    else:
      c=2
      print("clave invalida")
    i=i+1
  if c==2 and i==3:
    print("Tarjeta bloqueada")
    break
  else:
    print("saldo de cuenta $",sc)
    m=int(input("Monto que desea retirar $ "))
    if m <=sc and m <=saldo:
      ns=sc-m
      nc=saldo-m
      print("saldo cuenta=",ns)
      print("Saldo cajero=",nc)
      salir=input("oprima N para continuar ")
    else:
      print("monto no permitido")
      salir=input("oprima N para continuar ")
    if salir!=chr(78):
      break
    else:
      continue