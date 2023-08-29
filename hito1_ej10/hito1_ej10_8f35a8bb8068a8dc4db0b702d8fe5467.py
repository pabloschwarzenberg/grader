usuario=10334151
clave=1803
ca=1000000
cu=100000
c=1
if c>2:
  print("tarjeta bloqueada")
else:
  b = int(input("Ingrese clave: "))
  a = int(input("Ingrese usuario: "))
  while c<3:
    if a != clave: 
      c=c+1
      print("clave invalida")
    else:
      monto = int(input("Ingrese monto: "))
      if 0<monto<=100000:
        cosa1 = cu - monto
        cosa2 = ca - monto
        print("saldo cuenta= ",cosa1)
        print("saldo cajero= ",cosa2)
        break
      else:
        print("monto no permitido")

  else:
        print("tarjeta bloqueada")
