#Cajero Automático
usuario = int(input("Ingrese los digitos del usuario: "))

clave = int(input("Ingrese la clave: "))

I = 1
Saldo_Cajero = 1000000
Saldo_Usuario = 100000
Usuario_Correcto = 10334151
Clave_Correcta = 1803

luka20 = 20000
luka10 = 10000
luka5 = 5000


def bills(c,x):
  billetes = c // x
  resto = c % x
  return billetes,resto

while clave != Clave_Correcta:
  I += 1
  if clave == Clave_Correcta:
    print("clave valida")
    break

  if I > 3:
    break

  print("clave invalida")

  clave = int(input("Ingresa nuevamente "))

if I > 3:
  print("tarjeta bloqueada")

if usuario == Usuario_Correcto :

  if clave == Clave_Correcta:
    monto = int(input("¿que monto desea retirar?: "))

    if monto > Saldo_Usuario and monto > Saldo_Cajero:
      print("monto no perimitido")
    else:
      Saldo_Usuario -= monto
      Saldo_Cajero -= monto
      b, r = bills(monto,luka20)
      c , r = bills(r , luka10)
      j , r = bills(r, luka5)
      print("saldo total de la cuenta="+str(Saldo_Usuario))
      print("saldo total del cajero="+str(Saldo_Cajero))
      print("billetes20000="+str(b))
      print("billetes10000="+str(c))
      print("billetes5000="+str(j))
