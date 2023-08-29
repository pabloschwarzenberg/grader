#Cajero Automático
intento = 0
saldo_cajero = 1000000
veinte = 0
diez = 0
cinco = 0
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
        while retiro > 0:
          if veinte == 20:
            break
          retiro = retiro - 20000
          veinte = veinte + 1
        if retiro < 0:
          retiro = retiro + 20000
          veinte = veinte - 1
        while retiro > 0:
          if diez == 40:
            break
          retiro = retiro - 10000
          diez = diez + 1
        if retiro < 0:
          retiro = retiro + 10000
          diez = diez - 1
        while retiro > 0:
          if cinco == 40:
            break
          retiro = retiro - 5000
          cinco = cinco + 1
        print("billetes 20000=",veinte)
        print("billetes 10000=",diez)
        print("billetes 5000=",cinco)
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