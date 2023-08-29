#Cajero Automático
usuario = input("Ingrese usuario: ")
clave = input("Ingrese clave: ")
saldo = 1000000


cuent = 100.000

intentos = 0

while clave != 1803 and intentos <= 2 :

 print("clave invalida")
 clave = input("Ingrese clave: ")
 intentos +=1
 if intentos >= 2:
   print("tarjeta bloqueada")
   break

while usuario == 10334151 and clave == 1803 :
  monto = int(input("Monto a retirar: "))

  if monto >= cuent :
    print("monto no permitido")
  if monto <= cuent :
    cuent -= monto
    saldo -= monto
    print("saldo cuenta=",cuent)  
    print("saldo cajero=",saldo)      