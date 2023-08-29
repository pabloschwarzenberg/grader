saldo_cuenta = 100000
saldo_cajero = 1000000
contador = 0

opcion = "N"

bill_20 = 20
bill_10 = 40
bill_5 = 40





while opcion == "N":
    usuario = input("Ingrese usuario")
    clave = input("Ingrese contraseña")

    if(usuario=="10334151" and clave == "1803"):
        giro = int(input("Ingrese un giro"))
        if(giro<saldo_cajero):
                    if(giro<saldo_cuenta):
                        saldo_cajero = saldo_cajero-giro
                        saldo_cuenta = saldo_cuenta - giro
                        print("Saldo Cuenta=", saldo_cuenta)
                        print("Saldo Cajero=", saldo_cajero)
                        valor_giro = giro
                        if giro%20000 ==0:
                            cant_Billetes20 = int(giro/20000)
                            valor_giro = giro - int(giro/20000)*20000
                        else:
                            cant_Billetes20 =0

                        if valor_giro%10000 ==0:
                            cant_Billetes10 = int(valor_giro/10000)
                            valor_giro = valor_giro - int(valor_giro/10000)*10000
                        else:
                            cant_Billetes10 =0

                        if giro%5000 ==0:
                            cant_Billetes5 = int(valor_giro/5000)
                        else:
                            cant_Billetes5 =0
                        print("billetes 20000 =", cant_Billetes20)
                        print("billetes 10000 =", cant_Billetes10)
                        print("billetes 5000= ", cant_Billetes5)
                    
                        opcion = input("Ingrese N para continuar: ")
                    else:
                        print("Saldo insuficiente")
        else:
            print("Saldo insuficiente")
    if(clave != "1803"):
        print("Clave inválida")
        contador += 1
        if(contador==3):
            print("tarjeta bloqueadas")
            break