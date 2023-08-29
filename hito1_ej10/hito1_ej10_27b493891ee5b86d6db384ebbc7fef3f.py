#Cajero Automático
import sys
usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))
cajero = 1000000
cuenta = 100000
intento = 0
if usuario == 10334151:
 while intento < 2:
  if clave != 1803:
   intento = intento + 1
   print("clave invalida")
   clave = int(input("Ingrese su clave: "))
  if clave == 1803:
   print("clave valida")
   break
 else:
  print("tarjeta bloqueada")
  exit()

while usuario == 10334151 and clave == 1803:
  retiro = int(input("Monto a retirar: "))
  cuenta = 100000 - retiro
  if cuenta < 0:
   retiro = int(input("Monto a retirar: "))
   cuenta = 100000 - retiro
  else:
   print("['saldo cuenta=",cuenta,",'saldo cajero=",cajero-retiro)
   break