#Cajero Automático
def billetes(a,b):
  billetes = a // b
  resto = a % b
  return billetes,resto

usu = int(input("Ingrese el usuario: "))
cla= int(input("Ingrese su clave: "))

intentos = 1
saldocajero = 1000000
s_usuario = 100000
p = 10334151
q = 1803

while cla != p:
  intentos += 1
   
  if cla == q:
    print("clave incorrecta")
    break

  if intentos > 3:
    break

  print("clave invalida")
  cla = int(input("Ingrese de nuevo su clave: "))


if intentos > 3:
  print("tarjeta bloqueada")

if usu == p :
   
  if cla == q:
    monto = int(input("¿cuanto retirara?:"))
     
    if monto > s_usuario and monto > saldocajero:
      print("monto no perimitido")
    else:

      s_usuario -= monto
      saldocajero -= monto

      print("saldo cuenta="+str(s_usuario))
      print("saldo cajero="+str(saldocajero))