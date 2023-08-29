#Cajero Automático
usuario = int(input("Ingrese el usuario: "))

clave = int(input("Ingrese su clave: "))



intentos = 1

monto_cajero = 1000000

monto_usuario = 100000

usuario = 10334151

contraseña = 1803





billetes_de_20 = 20000

billetes_de_10 = 10000

billetes_de_5 = 5000





def bills(c,x):

  billetes = c // x

  resto = c % x

  return billetes,resto



while clave != contraseña:

  intentos += 1

   

  if clave == contraseña:

    print("clave incorrecta")

    break



  if intentos > 3:

    break



  print("clave invalida")

  clave = int(input("Ingrese de nuevo su clave: "))





if intentos > 3:

  print("tarjeta bloqueada")



if usuario == usuario :

   

  if clave == contraseña:

    monto = int(input("¿Cuanto quiere retirar?: "))

     

    if monto > monto_usuario and monto > monto_cajero:

      print("monto no perimitido")

    else:



      monto_usuario -= monto

      monto_cajero -= monto

      b, r = bills(monto,billetes_de_20)

      c , r = bills(r , billetes_de_10)

      j , r = bills(r, billetes_de_5)



      print("saldo cuenta="+str(monto_usuario))

      print("saldo cajero="+str(monto_cajero))

      print("billetes20000="+str(b))

      print("billetes10000="+str(c))

      print("billetes5000="+str(j))
