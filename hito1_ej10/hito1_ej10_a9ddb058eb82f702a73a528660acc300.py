#Cajero Automático
saldo=1000000
cuenta=100000
intentos=3
print("saldo en el cajero:")
print(saldo)
usuario=int(input("ingresa usuario: "))
clave=int(input("ingresa clave: "))
while intentos>0:
            if usuario==10334151 and clave==1803:
                    monto=(input("monto a retirar: "))
                    print("saldo en cuenta: ")
                    print(cuenta)
                        if monto=="Y":
                            exit()
                            break
                        else:
                            montonew=int(monto)
                            if montonew<=100000:
                                cuenta=cuenta-montonew
                                print("saldo cuenta= ")
                                print(cuenta)
                                saldo=saldo-montonew
                                print("saldo cajero= ")
                                print(saldo)
                            elif montonew>100000:
                                print("monto no permitido")
                            else:
                                print("no valido")
                                exit()
                                break
            elif intentos==0:
                print("tarjeta bloqueada")
                exit()
                break
            else:
                print("clave invalida")
                intentos=intentos-1