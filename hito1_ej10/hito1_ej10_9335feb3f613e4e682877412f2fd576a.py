#Cajero Automático
user = int(input("Ingrese usuario: "))
clave = int(input("Ingrese clave: "))
saldoinicialcajero = 1000000
saldoinicialcuenta = 100000

while user != 10334151:
    usuario = int(input("Error, Ingrese usuario nuevamente: "))
intentos = 0
while not(clave == 1803):
    intentos = intentos + 1
    if intentos == 3:
        print("Error,Tarjeta Bloqueada.")
        break
    else :
         clave = int(input("Error,Ingrese su clave: "))

if intentos != 3:
    print("continue")
montoR = int(input("Ingrese monto a retirar: ")) 

if montoR> 100000:
    print("Monto no permitido.")

elif montoR<100000:
    saldoinicialcuenta = saldoinicialcuenta - montoR
    saldoinicialcajero = saldoinicialcajero - montoR
    print("saldo cuenta=",saldoinicialcuenta)
    print("saldo cajero=",saldoinicialcajero)
    



