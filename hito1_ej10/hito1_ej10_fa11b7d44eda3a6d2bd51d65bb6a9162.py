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
    print("Ingrese el monto a retirar")
    monto = input()
else:
  print("tarjeta bloqueada")