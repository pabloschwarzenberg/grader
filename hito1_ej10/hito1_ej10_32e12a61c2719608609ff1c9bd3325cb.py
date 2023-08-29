#Cajero Automático

cuenta = 0
while cuenta < 3:
  usuario = int(input())
  clave = int(input())
  if usuario == 10334151 and clave == 1803:
    monto_cajero = 1000000
    monto = 100000
    monto_a_retirar = int(input())
    if monto_a_retirar >= monto:
      print("monto no permitido")
    else:
      monto = monto - monto_a_retirar
      monto_cajero = monto_cajero - monto_a_retirar
      print("saldo cuenta={}".format(monto))
      print("saldo cajero={}".format(monto_cajero))
  
  elif clave != 1803 and usuario!="N":
    print("clave invalida")
    cuenta += 1
    usuario = 10334151
    
if cuenta == 3:
  print("tarjeta bloqueada")