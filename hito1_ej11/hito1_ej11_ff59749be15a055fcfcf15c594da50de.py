#Cajero Automático
saldocajero = 1000000
saldocuenta = 100000
b20=20
b10=40
b5=40
usuario = int(input("Ingrese usuario: "))
while usuario != 10334151:
  usuario = int(input("Ingrese usuario: "))
clave = int(input("Ingrese clave: "))
intentos=0
while (clave!=1803):
  intentos = intentos+1
  if intentos == 3:
    print("Tarjeta bloqueada")
    break
  else:
    clave = int(input("Clave invalida: "))
if intentos != 3:
  respuesta ="n"
  while (respuesta == "n"):
    monto = int(input("Monto a retirar: "))
    if monto>saldocuenta or monto>saldocajero:
      print("Monto no permitido")
    else:
      retirab20 = 0
      retirab10 = 0
      retirab5 = 0
      saldocajero = saldocajero - monto
      saldocuenta = saldocuenta - monto
      while(monto>0):
        if monto >= 20000 and b20>0:
          retirab20 = retirab20 + 1
          b20 = b20 - 1
          monto = monto-20000
        if monto >= 10000 and b10>0:
          retirab10 = retirab10 + 1
          b10 = b10 - 1
          monto = monto-10000
        if monto >= 5000 and b5 > 0:
          retirab5 = retirab5 + 1
          b5 = b5 - 1
          monto = monto-5000
      print("saldo cuenta="+str(saldocuenta))
      print("saldo cajero="+str(saldocajero))
      print("billetes 20000="+str(retirab20))
      print("billetes 10000="+str(retirab10))
      print("billetes 5000="+str(retirab5))
      respuesta = input("Si quiere volver a operar ingrese (n), si no, ingrese cualquier otra letra: ")
      