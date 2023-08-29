#Cajero Automático
i=0
Saldo=1000000
while True:
  user=int(input("Ingrese usuario: "))
  clave=int(input("Ingrese clave: "))

  if i<3 and clave==1803:
    MR=int(input("Ingrese monto a retirar: "))
    if MR>100000:
      print("Monto no permitido")
      continue
    elif MR<=100000:
      Monto=100000-MR
      print("saldo cuenta=", Monto)
      Saldo-=MR
      print("saldo cajero=", Saldo)
  elif clave!=1803:
    print("clave invalida")
    i=i+1
    if i>=3 and clave!=1803:
      print("tarjeta bloqueada")
      break
  