saldocuenta = 100000
saldocajero = 1000000
i = 0

user = eval(input("Nombre de usuario: "))
while True:
    contrasena = eval(input("Contraseña: "))
    
    if contrasena == 1803:
        retiro = eval(input("Monto que desea retirar: "))
        if retiro <= saldocuenta:
            saldocuenta = saldocuenta - retiro
            saldocajero = saldocajero - retiro
        else:
            print("monto no permitido")
        break
    else:
        i += 1
        print("clave invalida")
        if i == 3:
            print("tarjeta bloqueada")
            break
print("saldo cuenta=",saldocuenta)
print("saldo cajero=",saldocajero)