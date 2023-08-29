#Cajero Automático
clave_1 = 1803
saldo_cajero = 1000000
saldo_cliente = 0


usuario = int(input("Ingrese Nombre de Usuario: "))
clave = int(input("Ingrese Clave: "))

if usuario == 10334151 and clave == clave_1:
 saldo_cliente = 100000
 while True:
    retiro = int(input("monto que desea retirar:"))
    if retiro > saldo_cliente:
      print("monto no valido")
      retiro = int(input("monto que desea retirar:"))
    if retiro < saldo_cliente:
      saldo_cliente = saldo_cliente - retiro
      saldo_cajero = saldo_cajero - retiro
      print("saldo cuenta=",saldo_cliente)
      print("saldo cajero=",saldo_cajero)
      break

if usuario == 10334151 and clave != clave_1:
  intentos_realizados = 0
  while clave != clave_1:
     print("Clave invalida")
     clave = int(input("Ingrese Clave: "))
     intentos_realizados += 1
     if intentos_realizaos == 2:
       print("Tarjeta bloqueada")
       break
      
      
     if clave == clave_1:
      saldo_cliente = 100000
      while True:
        retiro = int(input("Monto que desea retirar:"))
        if retiro > saldo_cliente:
          print("No tiene esa cantidad")
          retiro = int(input("Monto que desea retirar:"))
        if retiro < saldo_cliente:
          saldo_cliente = saldo_cliente - retiro
          saldo_cajero = saldo_cajero - retiro
          print("Saldo cuenta=",saldo_cliente)
          print("Saldo cajero=",saldo_cajero)
          break


   