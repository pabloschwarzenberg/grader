intentos = 0
clave = 1803
usuario_valido = 10334151
saldo_cajero = 1000000
saldo_cuenta = 100000
billetesde20 = 20000
billetesde10 = 10000
billetesde5 = 5000
cantidadbilletesde20 = 20
cantidadbilletesde10 = 40
cantidadbilletesde5 = 40

while intentos <= 3:

  usuarioi = int(input("Ingrese su usuario: "))
  clavei = int(input("Ingrese su clave: "))

  if intentos == 3:
    print("tarjeta bloqueda")
    break

  elif clavei == clave:
    monto = int(input("Ingrese un monto a retirar: "))

    while True:
      if monto < 0:
        print("monto no permitido")

      else:
        saldo_cajero = saldo_cajero - monto
        saldo_cuenta = saldo_cuenta - monto


        if (cantidadbilletesde20 * billetesde20) + (cantidadbilletesde10 * billetesde10) + (cantidadbilletesde5 * billetesde5) < monto:
          print("No hay suficientes billetes para cubrir el costo total.")
        else:
          # Calcular la cantidad de billetes necesarios para cada denominación
          billetes20 = min(monto // billetesde20, cantidadbilletesde20)
          monto -= billetes20 * billetesde20
          billetes10 = min(monto // billetesde10, cantidadbilletesde10)
          monto -= billetes10 * billetesde10
          billetes5 = min(monto // billetesde5, cantidadbilletesde5)
          monto -= billetes5 * billetesde5


          print("billetes 20000=",billetes20)
          print("billetes 10000=",billetes10)
          print("billetes 5000=",billetes5)

          print("saldo cuenta=",saldo_cuenta)
          print("saldo cajero=",saldo_cajero)
      break

    break

  else:
    print("clave invalida")
    intentos = intentos + 1