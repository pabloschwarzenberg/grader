def distribucionBilletes(dinero, billete20, billete10, billete5):
    limite = 0
    while limite < dinero:
        if limite + 20000 <= dinero and billete20 != 0:
            limite += 20000
            billete20 -= 1
        elif limite + 10000 <= dinero and billete10 != 0:
            limite += 10000
            billete10 -= 1
        elif limite + 5000 <= dinero and billete5 != 0:
            limite += 5000
            billete5 -= 1
    return 20 - billete20, 40 - billete10, 40 - billete5


saldocuenta, saldocajero = 100000, 1000000
billete20, billete10, billete5 = 20, 40, 40
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
        elif dinero.isdigit() and saldocuenta > int(dinero):
            dinero = int(dinero)
            saldocuenta -= dinero
            saldocajero -= dinero
            billete20, billete10, billete5 = distribucionBilletes(dinero, billete20, billete10, billete5)
        else:
            print("monto no permitido")
            continue
        print(["saldo cuenta={}".format(saldocuenta),"saldo cajero={}".format(saldocajero)])
        print("billetes 20000={}\nbilletes 10000={}\nbilletes 5000={}".format(billete20, billete10, billete5))