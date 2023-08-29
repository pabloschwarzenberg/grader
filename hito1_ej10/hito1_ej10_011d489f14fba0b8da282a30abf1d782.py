#Cajero Automático
def bills(l,a):

  money = l // a

  diferencia= l % a

  return money,diferencia



usuario = int(input("Ingrese el usuario: "))

clave = int(input("Ingrese su clave: "))



intentos = 1

saldo_cajero = 1000000

saldo_usuario = 100000

cliente = 10334151

cifra = 1803



billetes_20 = 20000

billetes_10 = 10000

billetes_5 = 5000





while clave != cifra:

  intentos += 1

   

  if clave == cifra:

    print("clave incorrecta")

    break



  if intentos > 3:

    break



  print("clave invalida")

  clave = int(input("Ingrese de nuevo su clave: "))





if intentos > 3:

  print("tarjeta bloqueada")



if usuario == cliente :

   

  if clave == cifra:

    monto = int(input("¿Cuanto quiere retirar?: "))

     

    if monto > saldo_usuario and monto > saldo_cajero:

      print("monto no perimitido")

    else:



      saldo_usuario -= monto

      saldo_cajero -= monto

      b, r = bills(monto,billetes_20)

      l , r = bills(r , billetes_10)

      j , r = bills(r, billetes_5)



      print("saldo cuenta="+str(saldo_usuario))

      print("saldo cajero="+str(saldo_cajero))