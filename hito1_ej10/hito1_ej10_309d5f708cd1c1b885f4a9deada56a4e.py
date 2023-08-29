#Cajero Automático
saldoCajero = 1000000

saldoUsuario = 100000

usu = "10334151"

passw = "1803"

intentos = 0

salir = False



while intentos < 3:

 if salir == True:

  break

 usuario = input("Ingrese el usuario")

 clave = input("Ingrese la clave")

 if usuario == usu and passw == clave:

  while True:

    

   monto = eval(input("Ingrese el monto"))

   if monto > saldoUsuario:

    print("monto no permitido")

   else:

    saldoUsuario = saldoUsuario - monto

    saldoCajero = saldoCajero - monto

    print("saldo cuenta=", saldoUsuario)

    print("saldo cajero=", saldoCajero)

   opcion = input("Desea Salir Y/N")

   if not(opcion == "N"):

    salir = True

    break

     

 else: 

  print("clave invalida")

  intentos = intentos + 1

if intentos == 3:

 print("tarjeta bloqueada")     