#Cajero Automático
usuar = int(input("Ingresa tu usuario: "))
clav = int(input("Ingresa tu clave: "))
cajero = 1000000
usuario = 10334151
clave = 1803
contador = 1
cuenta = 100000

if clav == clave:
  n = int(input("Cuanto quieres retirar: "))
  if n < cajero and n <= cuenta:
    montocajero = cajero - n
    montouser = cuenta - n
    print("saldo cuenta= ", montouser)
    print("saldo cajero= ", montocajero)
  else:
    print("monto invalido")
elif contador <= 3 :
  print("clave invalida")
  contador = contador + 1
elif contador > 3:
  print("Tarjeta bloqueada")