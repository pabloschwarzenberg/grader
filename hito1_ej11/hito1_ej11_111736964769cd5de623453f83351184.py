#Cajero Automático
saldoCajero = 1000000
saldoUsuario = 100000
usu = "10334151"
passw = "1803"
intentos = 0
salir = False
while intentos < 3:
 if salir == True:
  break
 usuario = input("Ingrese el usuario")
 clave = input("Ingrese la clave")
 if usuario == usu and passw == clave:
  while True:   
   monto = eval(input("Ingrese el monto"))
   if monto > saldoUsuario:
    print("monto no permitido")
   else:
    saldoUsuario = saldoUsuario - monto
    saldoCajero = saldoCajero - monto
    print("saldo cuenta=", saldoUsuario)
    print("saldo cajero=", saldoCajero)
   opcion = input("Desea Salir Y/N")
   if not(opcion == "N"):
    salir = True
    break     
 else: 
  print("clave invalida")
  intentos = intentos + 1
if intentos == 3:
 print("tarjeta bloqueada")
b20k = 20
b10k = 40
b5k = 40
b20ku = 0
b10ku = 0
b5ku = 0
while monto >=20000:
 monto = monto - 20000
 b20k -= 1
 b20ku += 1
while monto >=10000:
 monto = monto - 10000
 b10k -= 1
 b10ku += 1
while monto >=5000:
 monto = monto - 5000
 b5k -= 1
 b5ku += 1
print("billetes 20000=",b20ku)
print("billetes 10000=",b10ku)
print("billetes 5000=",b5ku)