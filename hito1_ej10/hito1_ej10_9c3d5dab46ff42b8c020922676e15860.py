#Cajero Automático
dinero_cajero = 1000000
usuario = int(input("ingrese su numero de usuario: "))
clave = int(input("ingrese su clave: "))
contador = 0
while usuario != 10334151 or clave != 1803:
    contadorr += 1
    print("clave invalida")
    if contador == 3:
       print("tarjeta bloqueada")
       break
    usuario = int(input("Ingrese su numero de usuario nuevamente: "))
    clave = int(input("ingrese su clave nuevamente: "))

if contador < 3:
    saldo_cuenta = 100000
while True:
  retiro = int(input("ingrese el total a retirar: "))
  if retiro == "N":
      break
  elif int(retiro) > dinero_cajero or int(retiro) <= 0 or int(retiro) > saldo_cuenta:
       print("monto invalido")
  else:
      dinero_cajero = dinero_cajero - int(retiro)
  saldo_cuenta -= int(retiro)
  print("saldo cuenta =" + str(saldo_cuenta))
  print("saldo cajero =" + str(dinero_cajero))
  break