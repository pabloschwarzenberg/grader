#Cajero Automático
def bills(m,n):

  bills = m// n

  o = m % n

  return bills,o


user = int(input("Ingrese el usuario: "))

clave = int(input("Ingrese su clave: "))


intentos = 1

cajero = 1000000

s_usuario = 100000

user1 = 10334151

password = 1803



bills_20 = 20000

bills_10 = 10000

bills_5 = 5000



while clave != password:

  intentos += 1

   

  if clave == password:

    print("clave incorrecta")

    break



  if intentos > 3:

    break



  print("clave invalida")

  clave = int(input("Ingrese de nuevo su clave: "))





if intentos > 3:

  print("tarjeta bloqueada")



if user == user1 :

   

  if clave == password:

    monto = int(input("¿Cuanto quiere retirar?: "))

     

    if monto > s_usuario and monto > cajero:

      print("monto no perimitido")

    else:



      s_usuario -= monto

      cajero -= monto

      y, u = bills(monto,bills_20)

      w , u = bills(u , bills_10)

      s , u = bills(u, bills_5)



      print("saldo cuenta="+str(s_usuario))

      print("saldo cajero="+str(cajero))

      print("billetes20000="+str(y))

      print("billetes10000="+str(w))

      print("billetes5000="+str(s))      