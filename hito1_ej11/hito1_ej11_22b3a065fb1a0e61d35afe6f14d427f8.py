usuario = int(input("Ingrese el usuario: "))

clave = int(input("Ingrese su clave: "))



intentos = 1

scajero = 1000000

susuario = 100000

user = 10334151

passw = 1803





billetes_20 = 20000

billetes_10 = 10000

billetes_5 = 5000





def bills(c,x):

  billetes = c // x

  resto = c % x

  return billetes,resto



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
      b, r = bills(monto,billetes_20)
      c , r = bills(r , billetes_10)
      j , r = bills(r, billetes_5)
      print("saldo cuenta="+str(susuario))
      print("saldo cajero="+str(scajero))
      print("billetes20000="+str(b))
      print("billetes10000="+str(c))
      print("billetes5000="+str(j))
