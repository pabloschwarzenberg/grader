#Cajero Automático
import sys

cuenta = {'usuario': '10334151', 'clave': '1803', 'saldo': 10000}
cajero = {'saldo': 1000000}

salir = "N"

while salir == "N":
    usuario = str(input("Ingrese su numero de usuario: "))
    clave = str(input("Ingrese su clave: "))


    intento = 1
    while clave != cuenta['clave']:
        print("clave invalida")
        intento = intento + 1
        clave = str(input("Ingrese su clave: "))
        if intento == 3:
            print("tarjeta bloqueada")
            sys.exit()

    retirar = int(input("Ingrese monto a retirar: "))

    while retirar > cajero['saldo']:
        print("monto no permitido")
        retirar = int(input("Ingrese monto a retirar: "))

    cuenta['saldo'] = cuenta['saldo'] + retirar
    cajero['saldo'] = cajero['saldo'] - retirar

    print("saldo cuenta={}".format(cuenta['saldo']))
    print("saldo cajero={}".format(cajero['saldo']))

    salir = input("Si desea repetir ingrese 'N', si desea salir ingrese cualquier otro valor: ")      