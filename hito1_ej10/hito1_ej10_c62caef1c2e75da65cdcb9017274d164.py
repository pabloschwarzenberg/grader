#Cajero Automático
intentos=0
SU= 100000
DCT= 1000000
usuarioA = int(input("por favor ingrese su usuario:"))
while usuarioA != 10334151 :
  usuarioA = int(input("Error,por favor vuelova a ingrsar su usuario:"))
  
claveA = int(input("por favor ingrese su clave:"))
while not(claveA == 1803):
    intentos = intentos+1
    if intentos ==3:
      print("tarjeta bloqueada")
      break
    else:
        claveA= int(input("ingrese su clave:"))

if intentos !=3:
   print("continue")

DineroR= int(input("ingrese su monto:"))

if DineroR <= DCT:
      if DineroR<= SU:
       DCT = DCT - DineroR
       SU = SU - DineroR
       print("saldo cuenta=", SU)
       print("saldo cajero=", DCT)
      else:
        print("monto invalido")
else:
    print("monto invalido")

respuesta = input("desea volver a hacer otra transaccion? (S/N)")