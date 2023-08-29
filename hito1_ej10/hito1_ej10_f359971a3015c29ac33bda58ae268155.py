saldoic = 100000
saldocajero = 1000000

usuario = str(input("Ingrese usuario: "))
clave = str(input("Ingrese clave: "))

 #contador
c = 0

if clave != "1803":

    print("Clave invalida, ingrese otra vez")

while clave != "1803" and c < 3:
    c = c + 1
    clave = str(input("Ingrese Clave: "))

    print("Tarjeta Bloqueada")

else:
    mr = int(input("Ingrese  monto a retirar: "))

    if mr > 100000:
      print("Monto no permitido")

      print("saldo cuenta=",saldoic)
      print("saldo cajero=",saldocajero)

    else:
      saldofc = saldoic - mr
      saldocajerof = saldocajero - mr

      print("saldo cuenta=",saldofc,",""saldo cajero=",saldocajerof)