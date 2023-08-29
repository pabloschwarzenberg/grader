def main():
    saldo_cajero = 1000000

    usuarios = {
        10334151: {"clave": 1803, "saldo": 100000}
    }

    intentos_fallidos = 0

    while True:
        usuario = int(input("Ingrese su usuario: "))
        clave = int(input("Ingrese su clave: "))

        if usuario in usuarios and clave == usuarios[usuario]["clave"]:
            print("¡Bienvenido!")
            saldo_cuenta = usuarios[usuario]["saldo"]

            while True:
                monto_retiro = int(input("Ingrese el monto a retirar: "))

                if monto_retiro <= 0:
                    print("Monto no permitido.")
                    
                elif monto_retiro > saldo_cuenta:
                    print("Saldo insuficiente.")
                    
                else:
                    saldo_cuenta -= monto_retiro
                    saldo_cajero -= monto_retiro
                    print("Saldo cuenta = ", saldo_cuenta)
                    print("Saldo cajero = ", saldo_cajero)
                    break

        else:
            intentos_fallidos += 1
            print("Usuario o clave incorrectos.")
            if intentos_fallidos >= 3:
                print("Tarjeta bloqueada.")
                break

        respuesta = input("¿Desea realizar otra operación? (S/N): ")
        if respuesta.upper() != "S":
            break

if __name__ == "__main__":
    main()