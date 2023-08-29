#Cajero Automático
intento = 0
saldo_cajero = 1000000
saldo_cuenta = 100000
retiro = 0
while intento != 3:
  user = int(input())
  pas = int(input())
  if user == 10334151 and pas == 1803:
    while True:
      retiro = int(input())
      if retiro <= saldo_cuenta:
        saldo_cuenta = saldo_cuenta - retiro
        saldo_cajero = saldo_cajero - retiro
        print("saldo cuenta=",saldo_cuenta)
        print("saldo cajero=",saldo_cajero)
        comando = input()
        if comando != "N":
          break
      else:
        print("monto no permitido")
  else:
    print("clave invalida")
    intento = intento + 1
  if intento == 3:
    print("tarjeta bloqueada")
    break
  break
