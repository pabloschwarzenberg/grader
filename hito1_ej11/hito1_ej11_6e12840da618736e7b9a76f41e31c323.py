class CajeroAutomatico:
    def __init__(self):
        self.saldo_cajero = {
            20000: 20,
            10000: 40,
            5000: 40
        }

    def validar_usuario(self, usuario, clave):
        if usuario == '10334151' and clave == '1803':
            return True
        else:
            return False

    def retirar_dinero(self, monto):
        billetes_entregados = {
            20000: 0,
            10000: 0,
            5000: 0
        }

        for billete in [20000, 10000, 5000]:
            cantidad_billetes = min(monto // billete, self.saldo_cajero[billete])
            monto -= cantidad_billetes * billete
            billetes_entregados[billete] = cantidad_billetes
            self.saldo_cajero[billete] -= cantidad_billetes

        if monto == 0:
            return True, billetes_entregados
        else:
            return False, billetes_entregados

cajero = CajeroAutomatico()
saldo_cuenta = 100000

intentos = 0
usuario = input("Ingrese el número de usuario: ")
clave = input("Ingrese la clave: ")

while intentos < 3:
    if cajero.validar_usuario(usuario, clave):
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= saldo_cuenta:
            exito, billetes_entregados = cajero.retirar_dinero(monto)
            if exito:
                saldo_cuenta -= monto
                print("Retiro exitoso.")
                print(f"Saldo cuenta: {saldo_cuenta}")
                print(f"Saldo cajero: {cajero.saldo_cajero}")
                for billete, cantidad in billetes_entregados.items():
                    print(f"Billetes {billete}: {cantidad}")
                break
            else:
                print("Monto no permitido.")
        else:
            print("Saldo insuficiente.")
    else:
        intentos += 1
        print("Clave inválida.")

if intentos == 3:
    print("Tarjeta bloqueada.")
