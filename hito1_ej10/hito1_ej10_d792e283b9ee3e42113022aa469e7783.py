usuarioEnBD = "10334151"
claveEnBD = "1803"
saldo = 100000
saldo_cajero = 1000000
usuario = input("Digite usuario: ")
clave = input("Digite contraseña: ")

if (clave==claveEnBD and usuario ==usuarioEnBD):
    retiro = int(input("Monto a retirar:"))
    if(saldo < retiro) and (saldo_cajero > retiro):
        print("Monto no permitido")
    else: saldo = (saldo - retiro) 
    if(saldo < retiro) and (saldo_cajero > retiro):
        print("Monto no permitido")
    else: saldo_cajero = (saldo_cajero - retiro)
    print("saldo cuenta=",saldo)
    print("saldo cajero=",saldo_cajero)
else: print("clave invalida")