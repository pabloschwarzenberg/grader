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
  respuesta ="s"
  
  while (respuesta == "s"):
    monto = int(input("Monto a retirar: "))
    
    if monto>saldocuenta or monto>saldocajero:
      print("Monto no permitido")

    else:

      bi20 = 0
      bi10 = 0
      bi5 = 0
      saldocajero = saldocajero - monto
      saldocuenta = saldocuenta - monto
      while(monto>0):

        if monto >= 20000 and b20>0:
          bi20 =  bi20 + 1
          b20 = b20 - 1
          monto = monto-20000

        if monto >= 10000 and b10>0:

          bi10 = bi10 + 1
          b10 = b10 - 1
          monto = monto-10000


        if monto >= 5000 and b5 > 0:

          bi5 = bi5 + 1
          b5 = b5 - 1
          monto = monto-5000


      print("saldo cuenta=",saldocuenta)

      print("saldo cajero=", saldocajero)

      print("billetes 20000=",bi20)

      print("billetes 10000=",bi10)

      print("billetes 5000=",bi5)

      respuesta = input("Quiere operar nuevamente\n (s) Para volver a operar\n (n)Para salir. ")      