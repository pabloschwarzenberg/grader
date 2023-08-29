#Cajero Automático
usuario = int(input("Ingrese el usuario: "))

clave = int(input("Ingrese su clave de acceso: "))



intentos = 1

saldo_del_cajero = 1000000

saldo_del_usuario = 100000

user = 10334151

password = 1803





billetes_de_20 = 20000

billetes_de_10 = 10000

billetes_de_5 = 5000





def bills(c,x):

  billetes = c // x

  resto = c % x

  return billetes,resto



while clave != password:

  intentos += 1

   

  if clave == password:

    print("La clave ingresada es incorrecta")

    break



  if intentos > 3:

    break



  print("La clave ingresada es invalida")

  clave = int(input("Ingrese de nuevo su clave: "))





if intentos > 3:

  print("La tarjeta ha sido bloqueada")



if usuario == user :

   

  if clave == password:

    monto = int(input("¿Cuanto quiere retirar?: "))

     

    if monto > saldo_del_usuario and monto > saldo_del_cajero:

      print("monto no perimitido")

    else:



      saldo_del_usuario -= monto

      saldo_del_cajero -= monto

      b, r = bills(monto,billetes_de_20)

      c , r = bills(r , billetes_de_10)

      j , r = bills(r, billetes_de_5)



      print("saldo cuenta="+str(saldo_del_usuario))

      print("saldo cajero="+str(saldo_del_cajero))

      print("billetes20000="+str(b))

      print("billetes10000="+str(c))

      print("billetes5000="+str(j))   