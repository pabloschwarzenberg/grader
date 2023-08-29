#Cajero Automático
numero_de_usuario1 = int(input("Ingrese el usuario: "))

contrasena = int(input("Ingrese su clave: "))



intentos = 1

saldo_cajero = 1000000

saldo_usuario = 100000

user = 10334151

passw = 1803





billetes_20 = 20000

billetes_10 = 10000

billetes_5 = 5000





def bills(c,x):

  billetes = c // x

  resto = c % x

  return billetes,resto



while contrasena != passw:

  intentos += 1

   
  if contrasena == passw:

    print("clave incorrecta")

    break



  if intentos > 3:

    break



  print("clave invalida")

  contrasena = int(input("Ingrese de nuevo su clave: "))





if intentos > 3:

  print("tarjeta bloqueada")



if numero_de_usuario1 == user :

   

  if contrasena == passw:

    monto = int(input("¿Cuanto quiere retirar?: "))

     

    if monto > saldo_usuario and monto > saldo_cajero:

      print("monto no perimitido")

    else:



      saldo_usuario -= monto

      saldo_cajero -= monto

      v, p = bills(monto,billetes_20)

      c , p = bills(p , billetes_10)

      t , p = bills(p, billetes_5)



      print("saldo cuenta="+str(saldo_usuario))

      print("saldo cajero="+str(saldo_cajero))

      print("billetes20000="+str(v))

      print("billetes10000="+str(c))

      print("billetes5000="+str(t))     