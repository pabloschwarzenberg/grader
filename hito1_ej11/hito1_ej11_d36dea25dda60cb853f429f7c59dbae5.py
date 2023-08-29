#Solicitud de clave y usuario usuario 10334151 y clave 1803
user = input("Ingrese su usuario: ")
password = ""
error = 0
solicitud = ""
saldo_cajero = 1000000
saldo_cuenta = 100000
while error < 3:  
  if password == "1803":
    while solicitud != "N":
      solicitud = input("Indique monto a retirar: ")
      if solicitud == "N":
        error = 1919322193
        break
      solicitud = int(solicitud)
      if solicitud > saldo_cajero:
        print("monto no permitido")
      else:
        saldo_cuenta = saldo_cuenta - int(solicitud)
        saldo_cajero = saldo_cajero - int(solicitud)
        print("saldo cuenta="+str(saldo_cuenta))
        print("saldo cajero="+str(saldo_cajero))
        m500 = solicitud//20000
        rest1 = solicitud - (m500*20000)
        m100 = rest1//10000
        rest2 = solicitud - ((m500*20000) + (m100*10000))
        m50 = rest2//5000
        rest3 = solicitud - ((m500*20000) + (m100*10000) + (m50*5000))
        print("billetes 20000="+str(m500))
        print("billetes 10000="+str(m100))
        print("billetes 5000="+str(m50))
  else:
    password = input("Ingrese su contrasena: ")
    if password != "1803":
      error += 1
      print("clave invalida")
if error == 3:
  print("tarjeta bloqueada")