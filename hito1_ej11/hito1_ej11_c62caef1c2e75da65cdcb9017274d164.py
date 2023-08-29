#Cajero Automático
intentos=0
SU= 100000
DCT= 1000000
bi20mil= 20
bi10mil= 40
bi5mil = 40 
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
   respuesta = "s"
while (respuesta == "s"):
  Retirar= int(input("ingrese su monto:")) 
  if Retirar <= DCT:
        if Retirar<= SU:
         DCT = DCT - Retirar
         SU = SU - Retirar
         retira20mil = 0
         retira10mil = 0
         retira5mil = 0
        while (Retirar>0):
          if Retirar >= 20000 and bi20mil>0:
              retirar20mil = retira20mil + 1
              bi20mil = bi20mil - 1
              Retirar = Retirar - 20000
              
          if Retirar >= 10000 and bi10mil>0:
              retirar10mil = retira10mil + 1
              bi10mil = bi10mil - 1
              Retirar = Retirar - 10000

          if Retirar >= 5000 and bi5mil>0:
              retirar5mil = retira5mil + 1
              bi5mil = bi5mil - 1
              Retirar = Retirar - 5000
              
        print("saldo cuenta=", SU)
        print("saldo cajero=", DCT)
        print("billetes 20000=", retira20mil)
        print("billetes 10000=", retira10mil)
        print("billetes 5000=", retira5mil)
   else:
     print("monto invalido")
else:
    print("monto invalido")

respuesta = input("desea volver a hacer otra transaccion? (S/N)")