#Cajero Automático
 def billetes(c,x):
  billetes = c // x
  resto = c % x
  return billetes,resto

usuario = int(input("Ingresar usuario: "))
clave = int(input("Ingresar clave: "))

intentos = 1
passw = 1803
user = 10334151
saldo_usuario = 100000
saldo_cajero = 1000000   


billetes_5 = 5000
billetes_10 = 10000
billetes_20 = 20000


while clave != passw:
  intentos += 1
   
  if clave == passw:
    print("clave invalida")
    break

  if intentos > 3:
    break
  print("clave invalida")
  clave = int(input("vuelva a ingresar su clave: "))


if intentos > 3:
  print("tarjeta bloqueada")

if usuario == user :
   
  if clave == passw:
    monto = int(input("¿Monto que desea retirar?: "))
     
    if monto > saldo_usuario and monto > saldo_cajero:
      print("monto no perimitido")
    else:

      saldo_usuario -= monto
      saldo_cajero -= monto

      b , r = billetes(monto,billetes_20)
      c , r = billetes(r , billetes_10)
      j , r = billetes(r, billetes_5)

      print("saldo cuenta="+str(saldo_usuario))
      print("saldo cajero="+str(saldo_cajero))


      print("billetes 20000="+str(b))
      print("billetes 10000="+str(c))
      print("billetes 5000="+str(j))     