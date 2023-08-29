#Cajero Automático
intentos=0
SU= 100000
DCT= 1000000
usuario = int(input("por favor ingrese su usuario:"))
while usuario != 10334151 :
  usuario = int(input("Error,por favor vuelova a ingrsar su usuario:"))

clave = int(input("por favor ingrese su clave:"))
while not(clave == 1803):
    intentos = intentos+1
    if intentos ==3:
      print("tarjeta bloqueada")
      break
    else:
        clave = int(input("ingrese su clave:"))

if intentos !=3:
   print("continue")

dinero = int(input("ingrese su monto:"))

if dinero <= DCT:
      if dinero <= SU:
       DCT = DCT - dinero
       SU = SU - dinero
       print("saldo cuenta=", SU)
       print("saldo cajero=", DCT)
      else:
        print("monto invalido")
else:
    print("monto invalido")

respuesta = input("desea volver a hacer otra transaccion? (S/N)")