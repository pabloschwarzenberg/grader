#Cajero Automático
import sys

src = int(input(""))
tar = input("")

if src != 10334151:
  print("Usuario inválido.")
  sys.exit(0)

x = 0
TempE = "N"
while TempE == "N":
  if tar != "1803":
    if x == 2:
      print("Tarjeta bloqueada.")
      x = 3
      sys.exit(0)
    else:
      tar = input("Clave inválida.")
    x += 1
  else:
    TempC = 1000000
    TempD = 100000
    TempA = input("¿Monto a retirar?")
    if TempA.isdigit():
      TempB = int(TempA)
    else:
      TempB = 0
    if TempB == 0 or TempB > TempC or TempB > TempD:
      print("Monto no permitido.")
      sys.exit(0)
    TempC -= TempB
    TempD -= TempB
    print("saldo cuenta=" + str(TempD))
    print("saldo cajero=" + str(TempC))
    TempE = input("¿Desea hacer otra operación?")