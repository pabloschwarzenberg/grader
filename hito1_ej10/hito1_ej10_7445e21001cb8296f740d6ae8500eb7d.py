# cajero
saldo_cajero = 1000000
saldo_cuenta = 100000

nro_cuenta = int(input("ingrese el nro de cuenta "))
contador = 0

if nro_cuenta != 10334151:
  print("numero de cuenta invalido ")
elif nro_cuenta == 10334151:
  print("numero de cuenta valido ")
  for contador in range(3):
    clave = int(input("por favor ingrese su clave "))
    if clave != 1803:
        print("clave invalida ")
        contador += 1
        if contador == 3:
          print("numero de intentos maximo alcanzado cuenta bloqueada ")
          break
    elif clave == 1803:
        print("clave valida")
        for contador in range(1):
          monto_retiro = int(input("ingrese el monto que quiere retirar de su cuenta "))
          if monto_retiro > 100000:
            print("saldo insuficiente")
            contador += 1
          elif monto_retiro <= 100000:
            saldo_cajero = saldo_cajero - monto_retiro
            saldo_cuenta = saldo_cuenta - monto_retiro
            print("saldo cuenta =",saldo_cuenta,"saldo cajero =",saldo_cajero)
    break