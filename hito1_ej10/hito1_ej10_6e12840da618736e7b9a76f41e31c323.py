   class CajeroAutomatico:
    def __init__(self):
        self.saldo_cajero = 1000000

    def validar_usuario(self, usuario, clave):
        if usuario == '10334151' and clave == '1803':
            return True
        else:
            return False

    def retirar_dinero(self, monto):
        if monto <= self.saldo_cajero:
            self.saldo_cajero -= monto
            return True
        else:
            return False

cajero = CajeroAutomatico()
saldo_cuenta = 100000

intentos = 0
usuario = input("Ingrese el número de usuario: ")
clave = input("Ingrese la clave: ")

while intentos < 3:
    if cajero.validar_usuario(usuario, clave):
        monto = float(input("Ingrese el monto a retirar: "))
        if monto <= saldo_cuenta:
            if cajero.retirar_dinero(monto):
                saldo_cuenta -= monto
                print("Retiro exitoso.")
                print(f"Saldo cuenta: {saldo_cuenta}")
                print(f"Saldo cajero: {cajero.saldo_cajero}")
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
