saldo_cajero = 1000000
saldo_usuario = 100000
intentos = 3
clave_invalida = True
usuario = input("Ingrese numero de usuario: ")
clave = input("Ingresa clave: ")
if usuario == "10334151":
 while clave_invalida and intentos > 1:
  if clave == "1803":
   clave_invalida = False
  else:
   clave_invalida = True
   print("clave invalida")
   intentos = intentos - 1
   clave = input("Ingrese clave: ")
  
 if clave == "1803":
  monto = input("Ingrese monto a retirar: ")
  monto = int(monto)
  saldo_cajero = saldo_cajero - monto
  saldo_usuario = saldo_usuario - monto
  if saldo_usuario >= 0:
   print("saldo cuenta=" + str(saldo_usuario)) 
   print("saldo cajero=" + str(saldo_cajero))
   salir = input("¿Desea salir?: ")
   if salir != "N":
    print("Operación realizada con éxito")
  else:
   print("monto no permitido")
 
 else:
  print("tarjeta bloqueada")