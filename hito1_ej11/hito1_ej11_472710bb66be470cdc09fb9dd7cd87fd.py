def bills(W,T):

  billss = W // T

  sustraccion_resta = W % T

  return billss,sustraccion_resta


Personaje = int(input("Ingrese el usuario: "))

key_code = int(input("Ingrese su clave: "))


procedimientos = 1

cajero_automatico = 1000000

saldode_personaje = 100000

USUARIO = 10334151

WORKPASS = 1803



billss_11 = 20000

billss_55 = 10000

billss_32 = 5000



while key_code != WORKPASS:

  procedimientos += 1

   

  if key_code == WORKPASS:

    print("clave incorrecta")

    break


  if procedimientos > 3:

    break


  print("clave invalida")

  key_code = int(input("Ingrese de nuevo su clave: "))



if procedimientos > 3:

  print("tarjeta bloqueada")


if Personaje == USUARIO :

   

  if key_code == WORKPASS:

    dinero_retirar = int(input("¿Cuanto quiere retirar?: "))

     

    if dinero_retirar > saldode_personaje and dinero_retirar > cajero_automatico:

      print("monto no perimitido")

    else:


      saldode_personaje -= dinero_retirar

      cajero_automatico -= dinero_retirar

      O, r = bills(dinero_retirar,billss_11)

      W , r = bills(r , billss_55)

      Q , r = bills(r, billss_32)


      print("saldo cuenta="+str(saldode_personaje))

      print("saldo cajero="+str(cajero_automatico))

      print("billetes20000="+str(O))

      print("billetes10000="+str(W))

      print("billetes5000="+str(Q))
 

  