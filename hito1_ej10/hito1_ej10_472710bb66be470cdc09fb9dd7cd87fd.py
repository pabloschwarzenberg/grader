def bills(Z,B):

  DINEROS = Z // B

  Sustraccion = Z % B

  return DINEROS,Sustraccion


PERSONA = int(input("Ingrese el usuario: "))

Contrasena = int(input("Ingrese su clave: "))


intentos = 1

Cajero = 1000000

Cuenta = 100000

USUARIO = 10334151

PASSWORK = 1803



DINEROS_70 = 20000

DINEROS_98 = 10000

DINEROS_0 = 5000



while Contrasena != PASSWORK:

  intentos += 1

   

  if Contrasena == PASSWORK:

    print("clave incorrecta")

    break


  if intentos > 3:

    break


  print("clave invalida")

  Contrasena = int(input("Ingrese de nuevo su clave: "))



if intentos > 3:

  print("tarjeta bloqueada")


if PERSONA == USUARIO :

   

  if Contrasena == PASSWORK:

    saldo_sacar = int(input("¿Cuanto quiere retirar?: "))

     

    if saldo_sacar > Cuenta and saldo_sacar > Cajero:

      print("monto no perimitido")

    else:


      Cuenta -= saldo_sacar

      Cajero -= saldo_sacar

      A, r = bills(saldo_sacar,DINEROS_70)

      Z , r = bills(r , DINEROS_98)

      K , r = bills(r, DINEROS_0)


      print("saldo cuenta="+str(Cuenta))

      print("saldo cajero="+str(Cajero))

      print("DINEROS20000="+str(A))

      print("DINEROS10000="+str(Z))

      print("DINEROS5000="+str(K))
     