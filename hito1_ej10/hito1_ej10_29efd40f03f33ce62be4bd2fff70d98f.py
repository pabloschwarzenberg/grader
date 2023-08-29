#Cajero Automático
saldoCajero = 1000000
validUser = 10334151
validPass = 1803
saldoCuenta = 100000
user = int(input("Ingrese usuario: "))

while user != validUser:
  user = int(input("Ingrese usuario nuevamente: "))

password = int(input("Ingrese clave: "))

intentos = 0
while password != validPass:
  intentos = intentos + 1
  if intentos == 3:
    print("Tarjeta bloqueada")
    break

  password = int(input("Clave inválida: "))

if intentos != 3:
  montoRetirado = int(input("Ingrese monto"))

  if montoRetirado>saldoCajero or montoRetirado>saldoCuenta:
    print("Monto no permitido")

  else:
    saldoCajero = saldoCajero - montoRetirado
    saldoCuenta = saldoCuenta - montoRetirado

    print("Saldo Cuenta=", saldoCuenta)
    print("Saldo Cajero=", saldoCajero)
