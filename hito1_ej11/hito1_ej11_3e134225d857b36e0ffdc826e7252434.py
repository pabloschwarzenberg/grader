#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = 10334151
clave = 1803
intentos_de_clave = 3
inicio = "I"
x=0
salir_programa = "N"
billetes_20000 = 0
billetes_10000 = 0
billetes_5000 = 0

while inicio == "I":
 
    while salir_programa =="N":
        
        if x < 4:
            ingresar_usuario = int (input("usuario: "))
            ingresar_clave = int(input("clave: "))

            if ingresar_clave == clave and ingresar_usuario == usuario:
                monto_a_retirar = int(input("Monto a retirar: "))

                if monto_a_retirar < saldo_cuenta:
                    saldo_cuenta = saldo_cuenta - monto_a_retirar
                    saldo_cajero = saldo_cajero - monto_a_retirar
                    desglose = monto_a_retirar
                    if desglose >= 20000:
                        queda = desglose // 20000
                        desglose = desglose % 20000
                        billetes_20000 = queda
                    if desglose >= 10000:
                        queda = desglose // 10000
                        desglose = desglose % 10000
                        billetes_10000 = queda
                    if desglose >=5000:
                        queda = desglose // 5000
                        desglose = desglose % 5000
                        billetes_5000 = queda

                    print("billetes 20000=" + str(billetes_20000))
                    print("billetes 10000=" + str(billetes_10000))
                    print("billetes 5000=" + str(billetes_5000))

                    print("saldo cuenta=" + str(saldo_cuenta))
                    print("saldo cajero=" + str(saldo_cajero))

                    salir_programa = input("Para continuar ingresar la letra N : " )
                else:
                    print("Monto no permitido")
            else:
                print("Clave invalida")
                x=x+1

        if x == intentos_de_clave:
            print("Tarjeta bloqueada")
            salir_programa = "s"  

    if salir_programa != "N":
        inicio = "s"