#Cajero Automático
usuario = int(input("ingrese su cuenta: "))
contador = 0
saldo_cajero= 1000000
saldo_cuenta= 100000
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
else:
  print("acceso denegado")