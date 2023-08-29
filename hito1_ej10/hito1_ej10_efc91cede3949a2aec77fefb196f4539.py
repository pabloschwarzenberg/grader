"""
13.- Tu cajero debe pedir un usuario y una clave para ingresar.
Al principio debe tener 1.000.000 como saldo inicial. Tu cajero debe dejar ingresar
al usuario 10334151 con la clave 1803, quien tiene al inicio del programa 100.000 en su cuenta.
Lo único que se puede hacer en este nivel es retirar dinero de la cuenta corriente. Tu programa
debe validar la clave y el monto a retirar, indicando el mensaje “clave invalida” cuando la clave
no corresponde y al tercer intento fallido debe indicar “tarjeta bloqueada” y salir del programa.
Si la clave es válida, debe preguntar por el monto a retirar. Cuando se hace el retiro de un monto
que no es válido debe indicar “monto no permitido”, si el monto se puede retirar debe actualizar
los saldos e imprimir el nuevo saldo que quedó en la cuenta corriente y el cajero, por ejemplo al
retirar 45.000 debiera imprimir:

•	saldo cuenta=55000
•	saldo cajero=955000

Tu programa debe repetirse continuamente, para salir la persona debe ingresar algo distinto a la letra “N”.
"""

dinero_cajero = 1000000
dinero_usuario = 100000
usuario = 10334151
usuario = int(input("Usuario: "))
clave = int(input("Clave: "))

if usuario == 10334151:
    tarjeta_bloqueada = False
    salir = "n"
    intentos = 1
    while not tarjeta_bloqueada and salir.lower() == "n":
        if clave == 1803:
            print("\nSaldo cuenta =", dinero_usuario)
            print("Saldo cajero =", dinero_cajero)
            while salir.lower() == "n":
                monto = input("\nMonto a retirar: ")
                while not monto.isdigit() or not int(monto) <= dinero_usuario or int(monto) <= 0:
                    print("Monto no permitido.")
                    monto = input("\nMonto a retirar: ")
                monto = int(monto)
                
                if dinero_cajero > 0 and monto <= dinero_cajero:
                    dinero_usuario -= monto
                    dinero_cajero -= monto
                    print("\nSaldo cuenta =", dinero_usuario)
                    print("Saldo cajero =", dinero_cajero)
                    salir = input("\nDesea salir? (Y/N): ")
                else:
                    if dinero_cajero == 0:
                        print("Cajero automático sin dinero. Vuelva más tarde.")
                        salir = "Y"
                    else:
                        print("El monto excede el dinero del cajero, elija otro monto.")
        else:
            print("Clave inválida.")
            intentos += 1
            clave = int(input("Clave: "))
        if intentos == 3:
            print("Tarjeta bloqueada.")
            tarjeta_bloqueada = True
else:
    print("Usuario no existente.")


     