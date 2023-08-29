#Cajero Automático
retiro = 0

respuesta = "N"

saldocajero = 1000000

saldocuenta = 100000

contador = 0

usuario1 = "10334151"

contraseña1 = "1803"

while respuesta == "N":
    
 usuario = str(input("Ingresar usuario: "))

 contraseña = str(input("Ingresar contraseña: "))

 while usuario != usuario1 or contraseña != contraseña1:

  contador = contador + 1
  print("clave invalida")

  if contador == 3:
   print("tarjeta bloqueada")
   break

  usuario = str(input("Ingresar usuario: "))

  contraseña = str(input("Ingresar contraseña: "))

 if contador != 3:

    retiro = int(input("Ingrese monto a retirar: "))

 if retiro <= saldocuenta and contador != 3:

  saldocuenta = saldocuenta - retiro

  saldocajero = saldocajero - retiro

  print("saldo cuenta= " + str(saldocuenta))

  print("saldo cajero= " + str(saldocajero))

 elif contador != 3:
      print("monto no permitido")
      

 respuesta = str(input("¿desea salir del programa?(Y/N)"))