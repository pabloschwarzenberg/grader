#Ahora tu cajero, además de hacer todo lo que debería hacer en el nivel 1, debe distribuir el monto a retirar entre los diferentes billetes que tiene disponibles, para ello al principio el saldo de 1.000.000 estará distribuido en 20 billetes de 20.000, 40 billetes de 10.000 y 40 billetes de 5.000. Cuando se haga un giro tu cajero además de imprimir los saldos, debe imprimir la cantidad de billetes que le entrega a la persona, por ejemplo al retirar 45.000 podría imprimir:
#billetes 20000=1
#billetes 10000=3
#billetes 5000=1

#Puedes distribuir los billetes de otra forma, lo importante es que la distribución cuadre con el monto solicitado.

saldo_inicial = 1000000
saldo_cajero = 1000000
intentos = 0
usuario_valido = False
billetes_20000 = 20
billetes_10000 = 40
billetes_5000 = 40

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    
    if usuario == "10334151" and clave == "1803":
        saldo_usuario = 100000
        usuario_valido = True
    else:
        intentos += 1
        print("Clave inválida.")
        if intentos == 3:
            print("Tarjeta bloqueada.")
            break  # Salir del bucle y finalizar el programa
    
    if usuario_valido:
        monto = int(input("Ingrese el monto a retirar: "))
        
        if monto <= 0:
            print("Monto no permitido.")
        elif monto > saldo_usuario or monto > saldo_cajero:
            print("Monto no permitido.")
        else:
            if monto % 5000 != 0:
                print("Monto no permitido.")
            else:
                # Cálculo de billetes necesarios
                billetes_20000_retirados = min(billetes_20000, monto // 20000)
                monto -= billetes_20000_retirados * 20000
                billetes_10000_retirados = min(billetes_10000, monto // 10000)
                monto -= billetes_10000_retirados * 10000
                billetes_5000_retirados = min(billetes_5000, monto // 5000)
                monto -= billetes_5000_retirados * 5000
                
                saldo_usuario -= (billetes_20000_retirados * 20000 +
                                  billetes_10000_retirados * 10000 +
                                  billetes_5000_retirados * 5000)
                saldo_cajero -= (billetes_20000_retirados * 20000 +
                                 billetes_10000_retirados * 10000 +
                                 billetes_5000_retirados * 5000)
                
                print("Saldo cuenta =", saldo_usuario)
                print("Saldo cajero =", saldo_cajero)
                
                print("Billetes 20000 =", billetes_20000_retirados)
                print("Billetes 10000 =", billetes_10000_retirados)
                print("Billetes 5000 =", billetes_5000_retirados)
                
                billetes_20000 -= billetes_20000_retirados
                billetes_10000 -= billetes_10000_retirados
                billetes_5000 -= billetes_5000_retirados
                
    opcion = input("¿Desea realizar otro retiro? (N para salir): ")
    if opcion.upper() != "N":
        break  # Salir del bucle y finalizar el programa
