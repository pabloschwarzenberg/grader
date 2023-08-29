#Cajero Automático
nombre_usuario_banco = int(input("Ingrese el usuario: "))

contrasena_usuario_banco = int(input("Ingrese su clave: "))

numero_de_intentos = 1
total_cajero_saldo = 1000000
total_user_saldo = 100000
numero_usuario = 10334151
contrasena_cajero = 1803

billetes_20 = 20000
billetes_10 = 10000
billetes_5 = 5000

def bills(c,x):
  billetes = c // x
  resto = c % x
  return billetes,resto

while contrasena_usuario_banco != contrasena_cajero:
  numero_de_intentos += 1
  if contrasena_usuario_banco == contrasena_cajero:
    print("clave incorrecta")
    break

  if numero_de_intentos > 3:
    break
  print("clave invalida")
  contrasena_usuario_banco = int(input("Ingrese de nuevo su clave: "))

if numero_de_intentos > 3:
  print("tarjeta bloqueada")
if nombre_usuario_banco == numero_usuario :
   
  if contrasena_usuario_banco == contrasena_cajero:
    monto = int(input("¿Cuanto quiere retirar?: "))
    
    if monto > total_user_saldo and monto > total_cajero_saldo:
      print("monto no perimitido")

    else:
      total_user_saldo -= monto
      total_cajero_saldo -= monto
      b, r = bills(monto,billetes_20)
      c , r = bills(r , billetes_10)
      j , r = bills(r, billetes_5)
      
      print("saldo cuenta="+str(total_user_saldo))
      print("saldo cajero="+str(total_cajero_saldo))
      print("billetes20000="+str(b))
      print("billetes10000="+str(c))
      print("billetes5000="+str(j))