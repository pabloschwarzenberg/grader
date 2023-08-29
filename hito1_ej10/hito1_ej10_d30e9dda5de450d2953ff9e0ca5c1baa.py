class CajeroAutomatico:
    def __init__(self):
        self.saldo_cajero = 1000000

    def validar_usuario(self, usuario, clave):
        if usuario == 10334151 and clave == 1803:
            return True
        return False

    def retirar_dinero(self, monto):
        if monto <= self.saldo_cajero:
            self.saldo_cajero -= monto
            return True
        return False

if __name__ == "__main__":
    cajero = CajeroAutomatico()
    saldo_cuenta = 100000
    intentos_fallidos = 0

    while True:
        usuario = int(input("Ingrese el número de usuario: "))
        clave = int(input("Ingrese la clave: "))

        if cajero.validar_usuario(usuario, clave):
            intentos_fallidos = 0
            monto = float(input("Ingrese el monto a retirar: "))
            if monto <= saldo_cuenta:
                if cajero.retirar_dinero(monto):
                    saldo_cuenta -= monto
                    print("Retiro exitoso")
                    print("Saldo cuenta:", saldo_cuenta)
                    print("Saldo cajero:", cajero.saldo_cajero)
                else:
                    print("Monto no permitido")
            else:
                print("Saldo insuficiente en la cuenta")
        else:
            intentos_fallidos += 1
            print("Clave inválida")

        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break

        opcion = input("¿Desea realizar otra transacción? (S/N): ")
        if opcion.upper() != "S":
            break

    print(["saldo cuenta=" + str(saldo_cuenta), "saldo cajero=" + str(cajero.saldo_cajero)])
