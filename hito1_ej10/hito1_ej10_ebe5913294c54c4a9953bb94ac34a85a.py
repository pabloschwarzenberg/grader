saldocuenta = 100000
saldocajero = 1000000
i = 1
clave = ""
while i <= 3:
    if i == 3:
        print("tarjeta bloqueada")
        break
    usuario = input("Ingrese usuario: ")
    clave = int(input("Ingrese constraseña: "))
    if clave == 1803:
        break
    elif clave != 1803:
        i += 1
        continue
if clave == 1803:
    while True:
        dinero = input("Ingrese monto a sacar: ")
        if dinero.isalpha() and dinero != "N":
            break
        if saldocuenta > int(dinero):
            saldocuenta -= int(dinero)
            saldocajero -= int(dinero)
        else:
            print("monto no permitido")
            continue
        print(["saldo cuenta={}".format(saldocuenta),"saldo cajero={}".format(saldocajero)])