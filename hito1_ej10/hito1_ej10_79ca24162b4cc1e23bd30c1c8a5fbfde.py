#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True
usuario=int(input("ingrese numero de usuario: "))
while usuario==10334151:
  clave=str("ingresa clave: ")
  while clave_invalida and intentos>1:
    if  clave=="1803":
        clave_invalida=False
    else:
        clave_invalida=True
        intentos=intentos-1
        clave=input("ingrese clave: ")

  if clave=="1803":
    monto=input("ingrese monto a retirar: ")
    monto=int(monto)
    while monto<=saldo_cuenta and monto<=saldo_cajero:
      while saldo_cajero>0 and saldo_cuenta>0:
        saldo_cajero=saldo_cajero-monto
        saldo_cuenta=saldo_cuenta-monto
        print("saldo cuenta=",saldo_cuenta,"saldo cajero=",saldo_cajero)
        break
      else:
        print("El cajero no tiene saldo suficiente")
    else:
      print("Monto no permitido")
    break
  else:
    print("tarjeta bloqueada")
  break