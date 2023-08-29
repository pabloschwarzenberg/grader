#Cajero Automático
b20 = 20
b10 = 40
b5 = 40
saldocajero = 1000000
saldouser = 100000

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
    userd = saldouser - retiro
    print("saldo cuenta=", userd, "saldo cajero=", cajero)
    retiro20 = 0
    retiro10 = 0
    retiro5 = 0
    while (retiro > 0):
        if retiro >= 20000 and b20 > 0:
            retiro20 = retiro20 + 1
            b20 = b20 - 1
            retiro = retiro - 20000
        if retiro >=10000 and b10 > 0:
            retiro10 = retiro10 + 1
            b10 = b10 - 1
            retiro = retiro - 10000
        if retiro >=5000 and b5 > 0:
            retiro5 = retiro5 + 1
            b5 = b5 - 1
            retiro = retiro - 5000
    print("saldo cuenta=",userd)
    print("saldo cajero=",cajero)
    print("billetes 20000=",retiro20)
    print("billetes 10000=", retiro10)
    print("billetes 5000=", retiro5)