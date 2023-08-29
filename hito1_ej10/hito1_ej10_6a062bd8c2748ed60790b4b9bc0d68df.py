def validar_clave(usuario, clave):
    if usuario == 10334151 and clave == 1803:
        return True
    else:
        return False

def retirar_dinero(monto, saldo_cuenta, saldo_cajero):
    if monto <= saldo_cuenta and monto <= saldo_cajero:
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("['saldo cuenta={0}','saldo cajero={1}]".format(saldo_cuenta,saldo_cajero))
    else:
        print("Monto no permitido.")

if __name__ == "__main__":
    usuario = 0
    clave = 0
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0

    while True:
        usuario = int(input("Ingrese su usuario: "))
        clave = int(input("Ingrese su clave: "))

        if validar_clave(usuario, clave):
            while True:
                monto = int(input("Ingrese el monto a retirar: "))

                if monto > 0:
                    retirar_dinero(monto, saldo_cuenta, saldo_cajero)
                    break
                else:
                    print("Monto no válido. Intente nuevamente.")

            respuesta = input("¿Desea realizar otra transacción? (S/N): ")
            if respuesta.upper() == "N":
                break
        else:
            intentos += 1
            print("Clave inválida.")

            if intentos == 3:
                print("Tarjeta bloqueada. Por favor, contacte al banco.")
                break


