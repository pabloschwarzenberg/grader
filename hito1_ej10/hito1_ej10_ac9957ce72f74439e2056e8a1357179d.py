#Cajero Automático
maquina = 1000000
saldo = 100000
error = 0
usuario = input("Ingrese usuario: ")
if usuario == "10334151":
  error = 0
  clave = input("Ingrese clave: ")
  while clave != "1803":
    error += 1
    print("clave invalida")
    if error == 3:
      print("tarjeta bloqueada")
      break
    clave = input("Ingrese clave: ")
if error != 3:
  retirada = input("Retiro: ")
seguirRetiro = input("Retirar? ")
while seguirRetiro == "Y":
  while error != 3 and usuario == "10334151":
    while not(int(retirada) <= saldo and int(retirada) <= maquina):
      print("monto no permitido")
      retirada = input("Retiro: ")
    maquina -= int(retirada)
    saldo -= int(retirada)
    print("saldo cuenta={}".format(saldo))
    print("saldo cajero={}".format(maquina))
    seguirRetiro = input("Retirar? ")
    if seguirRetiro != "Y":
      break
    retirada = input("Retiro: ")