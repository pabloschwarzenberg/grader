#Cajero Automático
Usuario = input()
Cajero = 1000000
Saldo = 100000

Errores = 0
while True:
  Clave = int(input())
  if Clave == 1803:
    break
  else:
    Errores = Errores + 1
    print("clave invalida")
  if Errores == 3:
    print("tarjeta bloqueada")
    break
if Errores < 3:
  while True:
    Monto = int(input())
    if Monto < Saldo and Monto > 0:
      print("saldo cuenta="+str(Saldo-Monto))
      print("saldo cajero="+str(Cajero-Monto))
      break