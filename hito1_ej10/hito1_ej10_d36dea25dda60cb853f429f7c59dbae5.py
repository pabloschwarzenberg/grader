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
      solicitud = int(input("Indique monto a retirar: "))
      if solicitud == "N" or solicitud == "Y":
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
  else:
    error += 1
    print("clave invalida")
    password = input("Ingrese su contrasena: ")
if error == 3:
  print("tarjeta bloqueada")
      