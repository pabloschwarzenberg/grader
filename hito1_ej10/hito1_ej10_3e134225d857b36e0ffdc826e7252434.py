#Cajero Automático

saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = 10334151
clave = 1803
intentos_de_clave = 3
inicio = "I"
x=0
salir_programa = "N"
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