pregunta = "N"
saldo_cajero = 1000000
saldo_cuenta = 100000
billetes_20 = 20
billetes_10 = 40
billetes_5 = 40

while pregunta == "N":


    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))
    contador_clave = 0

    while clave != 1803:
        contador_clave += 1
        print("Clave invalida")
        print()
        if contador_clave == 3:
            print("Tarjeta Bloqueada")
            exit()
        clave = int(input("Ingrese su clave: "))

    monto_retiro = int(input("Ingrese el monto a retirar: "))
    print()
    while monto_retiro > 1000000 or monto_retiro < 1 or monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
        print("Monto no permitido")
        print()
        monto_retiro = int(input("Ingrese el monto a retirar: "))
        print()

    entr_bill_20 = int(monto_retiro/20000)
    if entr_bill_20 != 0 and entr_bill_20 <= billetes_20:
        print("Billetes 20.000 = " + str(entr_bill_20))
        restante_entr_billetes = monto_retiro - entr_bill_20*20000
    
    entr_bill_10 = int(restante_entr_billetes/10000)
    if entr_bill_10 != 0 and entr_bill_10 <= billetes_10 and restante_entr_billetes <= monto_retiro:
        print("Billetes 10.000 = " + str(entr_bill_10))
        restante_entr_billetes = restante_entr_billetes - entr_bill_10*10000
    
    entr_bill_5 = int(restante_entr_billetes/5000)
    if entr_bill_5 !=0 and entr_bill_5 <= billetes_5 and restante_entr_billetes <= monto_retiro:
        print("Billetes 5.000 = " + str(entr_bill_5))
        restante_entr_billetes = restante_entr_billetes - entr_bill_5*5000

    monto_entregado = entr_bill_20*20000 + entr_bill_10*10000 + entr_bill_5*5000

    saldo_cajero = saldo_cajero - monto_entregado
    saldo_cuenta = saldo_cuenta - monto_entregado
    print()
    print("Saldo cuenta = " + str(saldo_cuenta))
    print("Saldo cajero = " + str(saldo_cajero))
    print()
    
    pregunta = input("¿Desea salir?: ")
