#Cajero Automático
intentos = 0
clave = 1803
usuario = 10334151
saldo_cajero = 1000000
saldo_cuenta = 100000

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

        print("saldo cuenta=",saldo_cuenta)
        print("saldo cajero=",saldo_cajero)
        break

    break

  else:
    print("clave invalida")
    intentos = intentos + 1     

   