#Cajero Automático
#Cajero Automático
usuario = input()
clave = input()
intentos = 0
while (clave != "1803" or usuario != "10334151") and intentos < 2:
  print("clave invalida")
  usuario = input()
  clave = input()
  intentos += 1
if intentos < 2:
  saldo = 100000
  print("Ingrese el monto a retirar")
  monto = input()
  while monto != "N":
    if(monto.isalpha()):
      break
    monto = int(monto)
    if monto > saldo:
      print("monto no permitido")
    else:
      saldo = saldo - monto
      print("saldo cuenta=", saldo)
      print("saldo cajero=", 900000 + saldo)
      print("billetes 20000=",monto // 20000)
      monto = monto - (monto // 20000)*20000
      print("billetes 10000=",monto // 10000)
      monto = monto - (monto // 10000)*10000
      print("billetes 5000=",monto // 5000)
      monto = monto - (monto // 5000)*5000
    print("Ingrese el monto a retirar")
    monto = input()
else:
  print("tarjeta bloqueada")   