#Cajero Automático
cuenta = 0
usuario = input("numero de usuario: ")
clave = input("ingrese clave secreta: ")
while cuenta < 3:
  if usuario == "10334151" and clave == "1803":
    monto_cajero = 1000000
    monto = 100000
    monto_a_retirar = input("monto a retirar:")
    if int(monto_a_retirar) >= monto:
      print("monto no permitido")
    else:
      monto = monto - int(monto_a_retirar)
      monto_cajero = int(monto_cajero) - int(monto_a_retirar)
      print("saldo cuenta={}".format(monto))
      print("saldo cajero={}".format(monto_cajero))
  
  elif clave != 1803 and usuario!="N":
    print("clave invalida")
    cuenta += 1
    usuario = 10334151
    
if cuenta == 3:
  print("tarjeta bloqueada")   