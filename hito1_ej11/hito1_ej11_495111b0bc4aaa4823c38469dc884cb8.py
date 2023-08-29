#Cajero Automático
import sys

cuenta = {'usuario': '10334151', 'clave': '1803', 'saldo': 10000}
cajero = {'saldo': 1000000, 'b20': 20, 'b10': 40, 'b5': 40}

billetes20 = 0
billetes10 = 0
billetes5 = 0

salir = "N"

# Inicio de programa #
while salir == "N":
    usuario = str(input("Ingrese su numero de usuario: "))
    clave = str(input("Ingrese su clave: "))


    # Fallar Clave #
    intento = 1
    while clave != cuenta['clave']:
        print("clave invalida")
        intento = intento + 1
        clave = str(input("Ingrese su clave: "))
        if intento == 3 and clave != '1803':
            print("tarjeta bloqueada")
            sys.exit()

    retirar = int(input("Ingrese monto a retirar: "))

    # Dinero disponible a retirar #
    while retirar > cajero['saldo'] or retirar < 5000 or retirar % 5000 != 0:
        print("monto no permitido")
        retirar = int(input("Ingrese monto a retirar: "))


    # Sacar dinero del cajero, y entregar a persona #
    cuenta['saldo'] = cuenta['saldo'] + retirar
    cajero['saldo'] = cajero['saldo'] - retirar

    # Distribución de billetes #

    cant_din = 0
    while cant_din < retirar:
        if retirar == 5000:
            cajero['b5'] = int(cajero['b5']) - 1
            cant_din = 5000
            billetes5 = 40 - int(cajero['b5'])

        elif retirar > 5000:
            if cajero['b5'] > 0 and cant_din < retirar:
                cajero['b5'] = int(cajero['b5']) - 1
                cant_din = cant_din + 5000
                billetes5 = 40 - int(cajero['b5'])
                print("BILETTE 5---", cajero['b5'], billetes5)

            if cajero['b10'] > 0 and cant_din < retirar and cant_din % 10000 == 0:
                cajero['b10'] = int(cajero['b10']) - 1
                cant_din = cant_din + 10000
                billetes10 = 40 - int(cajero['b10'])
                print("BILETTE 10---", cajero['b10'], billetes10)

            if cajero['b20'] > 0 and cant_din < retirar and cant_din % 20000 == 0:
                cajero['b20'] = int(cajero['b20']) - 1
                cant_din = cant_din + 20000
                billetes20 = 20 - int(cajero['b20'])
                print("BILETTE 20---", cajero['b20'], billetes20)


    # Mostrar por pantalla información #
    print("saldo cuenta={}".format(cuenta['saldo']))
    print("saldo cajero={}".format(cajero['saldo']))
    if billetes20 > 0:
        print("billetes 20000={}".format(billetes20))
    if billetes10 > 0:
        print("billetes 10000={}".format(billetes10))
    if billetes5 > 0:
        print("billetes 5000={}".format(billetes5))

    # Preguntar si finaliza #
    intento = 1
    salir = input("Si desea repetir ingrese 'N', si desea salir ingrese cualquier otro valor: ").upper()      