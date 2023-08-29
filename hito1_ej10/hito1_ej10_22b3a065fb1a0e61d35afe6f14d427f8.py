usuario = int(input("Ingrese el usuario: "))
clave = int(input("Ingrese su clave: "))

scajero = 1000000
susuario = 100000
user = 10334151
passw = 1803
intentos = 1
while clave != passw:

  intentos += 1

   

  if clave == passw:

    print("clave incorrecta")

    break



  if intentos > 3:

    break



  print("clave invalida")

  clave = int(input("Ingrese de nuevo su clave: "))





if intentos > 3:

  print("tarjeta bloqueada")



if usuario == user :

   

  if clave == passw:

    monto = int(input("¿Cuanto quiere retirar?: "))

     

    if monto > susuario and monto > scajero:

      print("monto no perimitido")

    else:
      susuario -= monto
      scajero -= monto
      print("saldo cuenta="+str(susuario))
      print("saldo cajero="+str(scajero))
    