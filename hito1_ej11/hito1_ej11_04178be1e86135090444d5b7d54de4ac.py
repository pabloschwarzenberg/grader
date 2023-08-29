#Cajero Automático
usuario = int(input("Ingrese USUARIO: "))
clave = int(input("Ingrese CLAVE: "))

#Al principio debe tener 1.000.000 como saldo inicial el cajero.
saldo_ini_cajero = 1000000
#Tu cajero debe dejar ingresar al usuario 10334151 con la clave 1803 quien tiene al inicio del programa 100.000 en su cuenta.
#Lo único que se puede hacer en este nivel es retirar dinero de la cuenta corriente.
saldo_ini_usu_1 = 100000
# usuario_1 = 10334151
# clave_1 = 1803
intento = 0
monto = 0
salida = "s"

#Tu programa debe validar la clave y el monto a retirar, indicando el mensaje “clave invalida” cuando la clave no corresponde
#y al tercer intento fallido debe indicar “tarjeta bloqueada” y salir del programa.
#Si la clave es válida, debe preguntar por el monto a retirar.
#Cuando se hace el retiro de un monto que no es válido debe indicar “monto no permitido”,
#si el monto se puede retirar debe actualizar los saldos e imprimir el nuevo saldo que quedó en la cuenta corriente y el cajero
#por ejemplo al retirar 45.000 debiera imprimir:
#     saldo cuenta=55000
#     saldo cajero=955000
while intento < 2:
    if usuario != 10334151 or clave != 1803:
        print("Clave Invalida -- ")
        print()
        clave = int(input("Ingrese CLAVE: "))
        intento +=1
    else:
        monto = int(input("Ingrese monto a retirar: "))
        if monto > 100000:
            print("Monto no permitido") 
        else:
            saldo_ini_usu_1 = saldo_ini_usu_1 - monto
            saldo_ini_cajero = saldo_ini_cajero - monto
            print()
            print("Saldo cuenta = " + str(saldo_ini_usu_1))
            print("Saldo cajero = " + str(saldo_ini_cajero))
            lista = [20000, 10000 , 5000]
            for x in lista:
                if monto >= x:
                    queda = monto // x
                    print("Billetes " + str(x) + " = " + str(queda))
                    monto = monto % x
            print()
            print("¿Desea realizar otra operación? ")  
    print("Marque (S) para finalizar o (C) para continuar: ")
    salida = input("Ingrese (S) o (C): ")
    if salida != "s":
        print()
    else:
        print("Gracias por su preferencia ")
    break


if intento == 2:
    print()
    print("Tarjeta Bloqueada ")
    print()
    print("Programa finalizado" )