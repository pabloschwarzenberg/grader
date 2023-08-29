#Cajero Automático
def bills(c,x):
  billetes = c // x
  resto = c % x
  return billetes,resto

usuario = int(input("Porfavor ingrese su usuario: "))
clave = int(input("Porfavor ingrese su clave: "))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
passw = 1803

bil_20k = 20000
bil_10k = 10000
bil_5k = 5000

while clave != passw:
  intentos += 1
  if clave == passw:
    print("clave incorrecta")
    break
  if intentos > 3:
    break
  print("clave invalida")
  clave = int(input("Ingrese de nuevo su clave: "))

if intentos > 3:
  print("tarjeta bloqueada")
if usuario == user :
  if clave == passw:
    monto = int(input("¿Cuanto quiere retirar?: "))
    if monto > saldo_usuario and monto > saldo_cajero:
      print("monto no permitido")
    else:
      saldo_usuario -= monto
      saldo_cajero -= monto
      b, r = bills(monto,bil_20k)
      c , r = bills(r , bil_10k)
      j , r = bills(r, bil_5k)

      print("saldo cuenta="+str(saldo_usuario))
      print("saldo cajero="+str(saldo_cajero))
      print("billetes 20000="+str(b))
      print("billetes 10000="+str(c))
      print("billetes 5000="+str(j))