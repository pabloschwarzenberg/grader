class CajeroAutomatico:
    def __init__(self):
        self.billetes = {20000: 20, 10000: 40, 5000: 40}
        self.saldo_total = 1000000

    def realizar_retiro(self, monto):
        if monto > self.saldo_total:
            print("Saldo insuficiente.")
            return

        billetes_entregados = {}
        for denominacion, cantidad in self.billetes.items():
            billetes_retirados = min(monto // denominacion, cantidad)
            monto -= billetes_retirados * denominacion
            self.billetes[denominacion] -= billetes_retirados
            billetes_entregados[denominacion] = billetes_retirados

        self.saldo_total -= monto

        if monto > 0:
            print("No es posible entregar el monto exacto con los billetes disponibles.")
        else:
            print("Retiro exitoso.")
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print(f"Billetes de ${denominacion}: {cantidad}")
            print(f"Saldo restante: ${self.saldo_total}")


cajero = CajeroAutomatico()

intentos_fallidos = 0

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == "10334151" and clave == "1803":
        print("Acceso permitido")
        break
    else:
        print("Clave inválida")
        intentos_fallidos += 1

    if intentos_fallidos >= 3:
        print("Tarjeta bloqueada")
        break

while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    cajero.realizar_retiro(monto_retiro)
