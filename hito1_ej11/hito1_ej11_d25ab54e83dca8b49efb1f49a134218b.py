def bills(a,b):

  billetes = a // b

  resto = a % b

  return billetes,resto



usuario = int(input("nombre de usuario: "))

clave = int(input("contraseña: "))



intentos = 1

saldo_cajero = 1000000

saldo_usuario = 100000

user = 10334151

passw = 1803





billetes_20 = 20000

billetes_10 = 10000

billetes_5 = 5000





while clave != passw:

  intentos += 1

   

  if clave == passw:

    print("clave incorrecta")

    break



  if intentos > 3:

    break



  print("clave invalida")

  clave = int(input("Ingrese de nuevo su contraseña: "))





if intentos > 3:

  print("tarjeta bloqueada")



if usuario == user :

   

  if clave == passw:

    monto = int(input("¿Cuanto desea retirar?: "))

     

    if monto > saldo_usuario and monto > saldo_cajero:

      print("monto incorrecto")

    else:



      saldo_usuario -= monto

      saldo_cajero -= monto

      b, r = bills(monto,billetes_20)

      a , r = bills(r , billetes_10)

      j , r = bills(r, billetes_5)



      print("saldo cuenta="+str(saldo_usuario))

      print("saldo cajero="+str(saldo_cajero))

      print("billetes20000="+str(b))

      print("billetes10000="+str(a))

      print("billetes5000="+str(j))