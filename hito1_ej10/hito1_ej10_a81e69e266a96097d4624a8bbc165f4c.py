#Cajero Automático
#entrada
#pedir al usuario su cuenta

#Salida:
#retirar el dinero de la cuenta corriente

saldocajero = 1000000
saldouser = 10000

print("Bienbenido Usuario")

user = int(input("ingrese su nombre de usuario: "))
while user != 10334151:
    user = int(input("ERROR, nombre de usuario invalido, ingrese otra vez: "))
contra = int(input("ingrese su constraseña: "))
intentos = 1
while contra != 1803:
    contra = int(input("Clave invalida: "))
    intentos = intentos+1
    print(intentos,"intentos")
    if intentos == 3:
        print("Tarjeta Bloqueada")
        break
if intentos != 3 :
    print("Bienvenido usuario:", user)
    print("Su Cuenta cuenta con:$",saldouser)
    print("El cajero tiene:$",saldocajero)
    retiro = int(input("Cuanto denero quiere retirar del cajero:"))
    while retiro >= saldocajero:
        retiro = int(input("Monto no valido, ingrese de nuevo la cantidad:"))
    cajero = saldocajero - retiro
    userd = retiro + saldouser
    print("saldo cuenta=",userd,"saldo cajero=",cajero)