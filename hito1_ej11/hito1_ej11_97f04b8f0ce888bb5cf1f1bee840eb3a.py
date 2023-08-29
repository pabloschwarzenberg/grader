#Cajero Automático
B20 = 20
B10 = 40
B5 = 40

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
      C20 = Monto//20000
      Monto = Monto - (20000*C20)
      C10 = Monto//10000
      Monto = Monto - (10000*C10)
      C5 = Monto//5000
      Monto = Monto - (5000*C5)
      print("billetes 20000="+str(C20))
      print("billetes 10000="+str(C10))
      print("billetes 5000="+str(C5))
      break