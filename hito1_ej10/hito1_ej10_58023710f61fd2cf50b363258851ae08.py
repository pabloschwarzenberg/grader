#Cajero Automático
intento = 0
saldo_cajero = 1000000
contador = 0
saldo_usuario = 100000
while contador == 0:
    while intento < 3 :
        usuario = int(input("Ingresa tu usuario:", ))
        clave = int(input("Ingresa su clave:", ))
        if (usuario == 10334151) and (clave == 1803):
            monto_retirar = int(input("Ingresa el monto que deseas retirar:",))

            if monto_retirar > saldo_usuario :
                print("monto no permitido")
                intento += 1
            if monto_retirar <= saldo_usuario :
                saldo_cajero = saldo_cajero - monto_retirar
                saldo_usuario = saldo_usuario - monto_retirar
                print("Saldo cajero = {}".format(saldo_cajero))
                print("Saldo cuenta = {}".format(saldo_usuario))
                opcion = input("Si desea continuar aprete N. Si no aprete cualquier letra.").upper()
                if opcion == "N":
                    contador = 0
                if opcion != "N":
                    contador = 1
                    break

        else:
            print("usuario o clave incorrecta")
            intento +=1
    if intento >=3:
        print("tarjeta bloqueada")
        break
print("Adios")
