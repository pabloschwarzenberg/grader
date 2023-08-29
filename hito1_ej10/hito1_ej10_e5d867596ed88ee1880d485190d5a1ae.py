def bills(c,x):
  billetes = c // x
  resto = c % x
  return billetes,resto

usuario = int(input("Ingrese el usuario: "))
clave = int(input("Ingrese su clave: "))

intentos = 1
saldocajero = 1000000
saldousuario = 100000
x = 10334151
y = 1803

while clave != y:
  intentos += 1
   
  if clave == y:
    print("clave incorrecta")
    break

  if intentos > 3:
    break

  print("clave invalida")
  clave = int(input("Ingrese de nuevo su clave: "))


if intentos > 3:
  print("tarjeta bloqueada")

if usuario == x :
   
  if clave == y:
    monto = int(input("¿Monto a retirar?: $"))
     
    if monto > saldousuario and monto > saldocajero:
      print("monto no perimitido")
    else:

      saldousuario -= monto
      saldocajero -= monto

      print("saldo cuenta="+str(saldousuario))
      print("saldo cajero="+str(saldocajero))
      
