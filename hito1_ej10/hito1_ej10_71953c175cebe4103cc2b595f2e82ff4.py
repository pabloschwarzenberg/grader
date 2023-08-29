#Cajero Automático
saldoCajero = 1000000
usaurioValido = 10334141
claveValida = 1083
saldoCuenta = 100000
usuario = int(input("ingrese usuario: "))
while usuario != usaurioValido:
  usuario = int(input("ingrese usuario: "))
intentos = 0
clave = int(input("Ingrese la clave: "))
while clave != claveValida:
  intentos = intentos + 1
  if(intentos == 3):
    print("tarjeta bloqueada")
    break
  clave = int(input("ingrese la clave: "))

if(intentos != 3):
  montoRetirado = int(input("Ingrese monto: "))
  if montoRetirado > saldoCajero or montoRetirado > saldoCuenta:
    print("monto no permitido")
  else:
    saldoCajero = saldoCajero - montoRetirado
    saldoCuenta = saldoCuenta - montoRetirado
    print("saldo cuenta=", saldoCuenta)
    print("saldo cajero=", saldoCajero)