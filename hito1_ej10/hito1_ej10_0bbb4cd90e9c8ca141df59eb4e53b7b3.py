from operator import contains
pregunta = "N"

while pregunta == "N":
    saldo_cajero = 1000000
    saldo_cuenta = 100000

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
    while monto_retiro > 1000000 or monto_retiro < 1 or monto_retiro > saldo_cuenta or monto_retiro > saldo_cajero:
        print("Monto no permitido")
        print()
        monto_retiro = int(input("Ingrese el monto a retirar: "))

    saldo_cajero = saldo_cajero - monto_retiro
    saldo_cuenta = saldo_cuenta - monto_retiro

    print("Saldo cuenta = " + str(saldo_cuenta))
    print("Saldo cajero = " + str(saldo_cajero))

    pregunta = input("¿Desea salir?: ")