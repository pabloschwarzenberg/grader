#Cajero Automático
saldocajero=1000000
usuariovalido=10334151
clavevalida=1803
saldocuenta=100000
usuario=int(input("Ingrese usuario: "))

while not usuario == usuariovalido:
   usuario = int(input("Ingrese usuario nuevamente: "))
   
clave = int(input("Ingrese clave: "))
intentos = 0
while not clave == clavevalida:
  clave = int(input("clave invalida: "))
  intentos = intentos + 1
  if intentos == 3:
    print("tarjeta bloqueada")
    break

    
#retiro de cajero
retiro=int(input("ingrese monto a retirar:"))
while  retiro>saldocajero or retiro>saldocuenta or retiro<0:
   print("monto no permitido")
   retiro = int(input("ingrese monto a retirar nuevamente "))
               
saldocajero=saldocajero-retiro
saldocuenta=saldocuenta-retiro
print("saldo cuenta=",saldocuenta)
print("saldo cajero=",saldocajero)




   