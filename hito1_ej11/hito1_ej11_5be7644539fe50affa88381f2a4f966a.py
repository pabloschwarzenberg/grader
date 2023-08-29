usuario = int(input("ingrese su cuenta: "))
contador = 0
saldo_cajero= 1000000
saldo_cuenta= 100000
billetes_20k = 20
billetes_10k = 40
billetes_5k = 40
if usuario == 10334151:
    print("bienvenido")
    clave = int(input("ingrese su clave: "))
    if clave == 1803:
        monto_a_retirar = int(input("cuanto desea retirar: "))
        if monto_a_retirar > saldo_cuenta or monto_a_retirar > saldo_cajero:
            print("Monto no permitido")
        else:
            saldo_cajero = saldo_cajero - monto_a_retirar
            saldo_cuenta = saldo_cuenta - monto_a_retirar
            print("saldo cajero= ", saldo_cajero, "\n", "saldo cuenta= ", saldo_cuenta)
            billetes_20k = monto_a_retirar // 20000
            monto_a_retirar = monto_a_retirar % 20000
            billetes_10k = monto_a_retirar // 10000
            monto_a_retirar = monto_a_retirar % 10000
            billetes_5k = monto_a_retirar // 5000
            monto_a_retirar = monto_a_retirar % 5000
            print("billetes 20000= ", billetes_20k)
            print("billetes 10000= ", billetes_10k)
            print("billetes 5000= ", billetes_5k)

    if clave != 1803:
      while contador < 3 and clave != 1803:
        clave = int(input("ingrese clave: "))
        contador = contador + 1
        if contador == 3:
            print("tarjeta bloqueada")
      if contador < 3 and clave == 1803:
        monto_a_retirar = int(input("cuanto desea retirar: "))
        if monto_a_retirar > saldo_cuenta or monto_a_retirar > saldo_cajero:
          print("Monto no permitido")
        else:
            saldo_cajero = saldo_cajero - monto_a_retirar
            saldo_cuenta = saldo_cuenta - monto_a_retirar
            print("saldo cajero= ", saldo_cajero,"\n","saldo cuenta= ", saldo_cuenta)
            billetes_20k = monto_a_retirar // 20000
            monto_a_retirar = monto_a_retirar % 20000
            billetes_10k = monto_a_retirar // 10000
            monto_a_retirar = monto_a_retirar % 10000
            billetes_5k = monto_a_retirar // 5000
            monto_a_retirar = monto_a_retirar % 5000
            print("billetes 20000= ", billetes_20k)
            print("billetes 10000= ", billetes_10k)
            print("billetes 5000= ", billetes_5k)
else:
  print("acceso denegado")