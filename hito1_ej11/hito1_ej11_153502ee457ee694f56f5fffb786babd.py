#Cajero Automático
class cajero:
    saldo = 1000000
    billetes_20 = 20
    billetes_10 = 40
    billetes_5 = 40

    @staticmethod
    def ingresar():
        invalido = 0
        usuario.numero_cuenta = int(input("Ingrese su usuario: "))
        while usuario.numero_cuenta != 10334151:
            print("Ese no es el numero de cuenta")
            usuario.numero_cuenta = int(input("Ingrese su usuario: "))
        while invalido != 3:
            usuario.clave = int(input("Ingrese su clave: "))
            if usuario.clave != 1803:
                print("clave invalida")
                invalido += 1
            else:
                return cajero.retirar()
        print("tarjeta bloqueada")

    @staticmethod
    def retirar():
        while True:
            monto = int(input("ingrese el monto a retirar: "))
            if monto < cajero.saldo and monto < usuario.saldo:
                return cajero.imprimir(monto)
            else:
                print("monto no permitido")

    def imprimir(self):
        cajero.saldo -= self
        usuario.saldo -= self
        print("saldo cuenta=", usuario.saldo)
        print("saldo cajero=", cajero.saldo)
        return cajero.billetes(self)

    def billetes(self):
        print("hola")
        veinte = 0
        diez = 0
        cinco = 0
        x = self / 1000
        print(x)
        while (x - 20) >= 0:
            cajero.billetes_20 -= 1
            veinte += 1
            x = x-20
        while (x - 10) >= 0:
            cajero.billetes_10 -= 1
            diez += 1
            x = x-10
        while (x - 5) >= 0:
            cajero.billetes_5 -= 1
            cinco += 1
            x = x-5
        print(
            "billetes 20000=", veinte,
            "\n billetes 10000=", diez,
            "\n billetes 5000=", cinco
        )


class usuario:
    saldo = 100000
    numero_cuenta = ""
    clave = ""


cajero.ingresar()
