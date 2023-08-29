#Cajero Automático
saldocajero = 1000000
saldocuenta= 100000
usuario = int(input("Ingrese un usuario: "))
clave = int(input("Ingese su clave: "))
if usuario == 10334151:
  if clave == 1803:
    monto = int(input("Monto a retirar?: "))
    if monto > saldocajero:
      print("monto no permitido")
    else:
      saldofinalcuenta = saldocuenta - monto
      saldofinalcajero = saldocajero - monto
      print("saldo cuenta=",saldofinalcuenta)
      print("saldo cajero=",saldofinalcajero)
  else:
    print("Clave invalida")
else:
  print("Usuario invalido")