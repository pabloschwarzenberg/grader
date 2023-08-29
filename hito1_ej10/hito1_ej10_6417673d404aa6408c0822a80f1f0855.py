class CajeroAutomatico:
    def __init__(self):
        self.saldo_cuenta = 100000
        self.saldo_cajero = 1000000
        self.usuario_correcto = "10334151"
        self.clave_correcta = "1803"
        self.intentos_fallidos = 0

    def iniciar_sesion(self):
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")

        if usuario == self.usuario_correcto and clave == self.clave_correcta:
            print("Inicio de sesión exitoso.")
            self.realizar_retiros()
        else:
            self.intentos_fallidos += 1
            print("Clave inválida.")

            if self.intentos_fallidos == 3:
                print("Tarjeta bloqueada.")
            else:
                self.iniciar_sesion()

    def realizar_retiros(self):
        while True:
            monto = int(input("Ingrese el monto a retirar: "))

            if monto <= 0:
                print("Monto no permitido.")
            elif monto > self.saldo_cuenta:
                print("Saldo insuficiente.")
            else:
                self.saldo_cuenta -= monto
                self.saldo_cajero -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta =", self.saldo_cuenta)
                print("Saldo cajero =", self.saldo_cajero)

            opcion = input("¿Desea realizar otro retiro? (S/N): ")
            if opcion.upper() != "S":
                break

    def ejecutar(self):
        print("Bienvenido al Cajero Automático")
        self.iniciar_sesion()


cajero = CajeroAutomatico()
cajero.ejecutar()
