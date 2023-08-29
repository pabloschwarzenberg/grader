#Cajero Automático
import random

intentos = 0
clave_correcta = 1803
usuario_correcto = 10334151
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}
saldo_cuenta = 100000

while intentos < 3:
    usuario_ingresado = int(input("Ingrese su usuario: "))
    clave_ingresada = int(input("Ingrese su clave: "))

    if clave_ingresada == clave_correcta and usuario_ingresado == usuario_correcto:
        monto = int(input("Ingrese el monto a retirar: "))

        if monto < 0:
            print("Monto no permitido")
        elif monto > saldo_cuenta or monto > sum(b * q for b, q in saldo_cajero.items()):
            print("Saldo insuficiente")
        else:
            billetes_entregados = {}

            for billete, cantidad in sorted(saldo_cajero.items(), reverse=True):
                if monto >= billete:
                    cantidad_entregada = min(monto // billete, cantidad)
                    monto -= billete * cantidad_entregada
                    billetes_entregados[billete] = cantidad_entregada

            if monto == 0:
                saldo_cuenta -= sum(b * q for b, q in billetes_entregados.items())
                for billete, cantidad_entregada in billetes_entregados.items():
                    saldo_cajero[billete] -= cantidad_entregada

                print("Retiro exitoso")
                print("Saldo cuenta:", saldo_cuenta)
                print("Saldo cajero:", saldo_cajero)
                print("Billetes entregados:")
                for billete, cantidad_entregada in billetes_entregados.items():
                    print("billetes", billete, "=", cantidad_entregada)
            else:
                print("No se puede retirar el monto solicitado")
        break

    else:
        print("Credenciales inválidas")
        intentos += 1

if intentos >= 3:
    print("Tarjeta bloqueada")
