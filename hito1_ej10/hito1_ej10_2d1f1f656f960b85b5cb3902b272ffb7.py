#Cajero Automático
def bills(y,z):
  B = y//z
  R = y%z
  return B,R
Name = int(input("Ingrese el usuario: "))
Code = int(input("Ingrese su clave: "))
tent = 1
total = 1000000
mio = 100000
cuenta = 10334151
cat = 1803
while Code != cat:
  tent += 1
  if Code == cat:
    print("clave incorrecta")
    break
  if tent > 3:
    break
  print("clave invalida")
  Code = int(input("Ingrese de nuevo su clave: "))
if tent > 3:
  print("tarjeta bloqueada")
if Name == cuenta :
  if Code == cat:
    cantidad = int(input("¿Cuanto quiere retirar?: "))
    if cantidad > mio and cantidad > total:
      print("monto no perimitido")
    else:
      mio -= cantidad
      total -= cantidad
      print("Saldo cuenta="+str(mio))
      print("Saldo cajero="+str(total))
      