# Cajero Automático
saldo_cajero = 1000000
numero_cliente = 10334151
clave_cliente = 1803
uso_de_cajero = True
saldo_cliente = 100000
intentos_de_clave = 3
while uso_de_cajero == True:
    c = True
    d = False
    while intentos_de_clave > 0:
        clave = int(input("ingrese clave: "))
        if clave_cliente == clave:
            print("clave valida")
            intentos_de_clave = 0
            monto = int(input("ingrese monto a retirar: "))
            while d == False:
                if monto > saldo_cajero or monto > saldo_cliente:
                    print("monto no permitido")
                    d = False
                    break
                else:
                    saldo_cliente -= monto
                    saldo_cajero -= monto
                    a = str(saldo_cliente)
                    b = str(saldo_cajero)
                    print("saldo cuenta=" + a)
                    print("saldo cajero=" + b)
                    while c == True:
                        termino_de_operacion = input("Para salir, presione cualquier letra (excepto la letra N):")
                        if termino_de_operacion != "N":
                            c = False
                            intentos_de_clave = 3
                            break
                        elif termino_de_operacion == "N":
                            print("ingrese otro digito")
                    d = True
            break
        elif clave_cliente != clave:
            print("clave incorrecta")
            intentos_de_clave -= 1
            if intentos_de_clave == 0:
                print("tarjeta bloqueada")

      