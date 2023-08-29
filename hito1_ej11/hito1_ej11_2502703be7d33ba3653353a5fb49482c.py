class Cajero:
    def __init__(self, saldo_cajero=1000000):
        self.saldo_cajero = saldo_cajero
        self.usuarios = {10334151: {"clave": 1803, "saldo": 100000}}
        self.intentos = 3
        self.billetes = {20000: 20, 10000: 40, 5000: 40}

    def retirar_dinero(self, usuario, clave, monto):
        if usuario not in self.usuarios:
            return "Usuario no encontrado"
        if self.usuarios[usuario]["clave"] != clave:
            self.intentos -= 1
            if self.intentos == 0:
                exit("Tarjeta bloqueada")
            return "Clave inválida"
        if monto > self.usuarios[usuario]["saldo"] or monto > self.saldo_cajero:
            return "Monto no permitido"

        # Lógica para la distribución de billetes
        retiro_billetes = {}
        for denominacion in sorted(self.billetes.keys(), reverse=True):
            cantidad = monto // denominacion
            if cantidad > self.billetes[denominacion]:
                cantidad = self.billetes[denominacion]
            monto -= cantidad * denominacion
            self.billetes[denominacion] -= cantidad
            self.saldo_cajero -= cantidad * denominacion
            retiro_billetes[denominacion] = cantidad

        # Lógica para actualizar saldos
        self.usuarios[usuario]["saldo"] -= sum(billete * cantidad for billete, cantidad in retiro_billetes.items())

        retiro_billetes_str = "\n".join(f"billetes {denominacion}={cantidad}" for denominacion, cantidad in retiro_billetes.items())
        return f"{retiro_billetes_str}\nsaldo cuenta={self.usuarios[usuario]['saldo']}\nsaldo cajero={self.saldo_cajero}"

cajero = Cajero()

while True:
    usuario = int(input("Ingresa tu número de usuario: "))
    clave = int(input("Ingresa tu clave: "))
    monto = int(input("Ingresa el monto a retirar: "))
    print(cajero.retirar_dinero(usuario, clave, monto))
    respuesta = input("¿Quieres realizar otra operación? (N para no): ")
    if respuesta.upper() == "N":
        break
