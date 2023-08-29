usuario= 10334151
clave = 1803 

saldocuenta= 100000
saldocajero= 1000000

cont= 0

us= int(input("Ingrese el usuario: "))
cla=int(input("Ingrese su clave: "))
if us != usuario or cla != clave:
  cont = cont+1
  print("Datos ingresados no validos")
  us1 = int(input("Ingrese el usuario: "))
  cla1 = int(input("Ingrese su clave: "))
  if us1 != usuario or cla1 != clave:
    cont = cont + 1
    print("Datos ingresados no validos")
    us2 = int(input("Ingrese el usuario: "))
    cla2 = int(input("Ingrese su clave: "))
    if us2 != usuario or cla2 != clave:
        print("Cuenta Bloqueada")

if (us == usuario and cla == clave) or (us1 == usuario and cla1 == clave) or (us2 == usuario and cla2 == clave):
  monto = int(input("Cuanto desea retirar?: "))
  nuevosaldocuenta = saldocuenta - monto
  nuevosaldocajero = saldocajero - monto
  print("saldo cuenta=", nuevosaldocuenta)
  print("saldo cajero=", nuevosaldocajero)
