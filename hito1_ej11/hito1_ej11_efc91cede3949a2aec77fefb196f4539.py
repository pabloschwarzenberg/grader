"""
14.- Ahora tu cajero, además de hacer todo lo que debería hacer en el nivel 1, debe distribuir
el monto a retirar entre los diferentes billetes que tiene disponibles, para ello al principio
el saldo de 1.000.000 estará distribuido en 20 billetes de 20.000, 40 billetes de 10.000 y
40 billetes de 5.000. Cuando se haga un giro tu cajero además de imprimir los saldos, debe
imprimir la cantidad de billetes que le entrega a la persona, por ejemplo al retirar 45.000
podría imprimir:

•	billetes 20000=1
•	billetes 10000=3
•	billetes 5000=1

Puedes distribuir los billetes de otra forma, lo importante es que la distribución cuadre con el monto solicitado.
"""

dinero_cajero = 1000000
billetes_20mil = 20
billetes_10mil = 40
billetes_5mil = 40
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
                billetes_20mil_entregados = 0
                billetes_10mil_entregados = 0
                billetes_5mil_entregados = 0
                monto = input("\nMonto a retirar: ")
                while not monto.isdigit() or not int(monto) <= dinero_usuario or not (int(monto)%5000 == 0) or int(monto) <= 0:
                    print("Monto no permitido (sólo montos enteros múltiplos de 5000 que no superen el saldo de la cuenta).")
                    monto = input("\nMonto a retirar: ")
                monto = int(monto)
                if dinero_cajero > 0 and monto <= dinero_cajero:
                    dinero_usuario -= monto
                    dinero_cajero -= monto
                    monto_dividido = monto
                    while monto_dividido > 0:
                        while monto_dividido >= 20000 and billetes_20mil > 0:
                            billetes_20mil_entregados += 1
                            billetes_20mil -= 1
                            monto_dividido -= 20000
                        while monto_dividido >= 10000 and billetes_10mil > 0:
                            billetes_10mil_entregados += 1
                            billetes_10mil -= 1
                            monto_dividido -= 10000
                        while monto_dividido >= 5000 and billetes_5mil > 0:
                            billetes_5mil_entregados += 1
                            billetes_5mil -= 1
                            monto_dividido -= 5000

                    print("billetes 20000="+str(billetes_20mil_entregados))
                    print("billetes 10000="+str(billetes_10mil_entregados))
                    print("billetes 5000="+str(billetes_5mil_entregados))

                    print("saldo cuenta="+str(dinero_usuario))
                    print("saldo cajero="+str(dinero_cajero))
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


