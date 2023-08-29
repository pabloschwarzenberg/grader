#Cajero Automático
class CajeroAutomatico:
    def __init__(self):
        self.saldo_cajero = 1000000
        self.saldo_usuario = 100000
        self.intentos_fallidos = 0
        self.usuario_valido = False

    def ingresar_usuario(self, usuario, clave):
        if usuario == "10334151" and clave == "1803":
            self.usuario_valido = True
            print("Bienvenido, usuario 10334151.")
        else:
            self.intentos_fallidos += 1
            print("Usuario o clave inválidos.")

            if self.intentos_fallidos >= 3:
                print("Tarjeta bloqueada.")
                exit()

    def retirar_dinero(self, monto):
        if not self.usuario_valido:
            print("Por favor, inicie sesión para realizar operaciones.")
            return

        if monto > 0:
            if monto <= self.saldo_usuario:
                if monto <= self.saldo_cajero:
                    self.saldo_usuario -= monto
                    self.saldo_cajero -= monto
                    print("Retiro exitoso. Nuevo saldo en cuenta: $", int(self.saldo_usuario))
                    print("Nuevo saldo en el cajero: $", int(self.saldo_cajero))
                else:
                    print("Monto no disponible en el cajero.")
            else:
                print("Saldo insuficiente en su cuenta.")
        else:
            print("Monto no permitido.")


