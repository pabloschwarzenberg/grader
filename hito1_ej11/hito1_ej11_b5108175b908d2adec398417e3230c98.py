#Cajero Automático
#datos
usuario = 10334151
clave = 1803
saldo = 100000
res = "F"
intentos = 0
monto_cajero = 1000000
billeste20 = 20
billetes10 = 40
billetes5 = 40
bill20 = 0
bill10 = 0
bill5  = 0
#programa
usu = int(input("Ingrese su usuario", ))
if usuario == usu:
    while intentos < 3:
        pas = int(input("Ingrese su clave", ))
        intentos = intentos + 1
        if pas == clave:
            print("El saldo de la cuennta es", saldo)
            while res != "N":
                din = int(input("ingrese el dinero deseado",))
                while din > saldo:
                        print("Monto no permitido")
                        din = int(input("ingrese el dinero deseado", ))
                else:
                        saldo = saldo - din
                        monto_cajero = monto_cajero - din
                        if din >= 20000:
                            bill20 = din // 20000
                            din = din - (20000 * bill20)
                            if din >= 10000:
                                bill10 = din // 10000
                                din = din - (10000 * bill10)
                                if din >= 5000:
                                    bill5 = din // 5000
                                    din = din - (5000 * bill5)
                            else:
                                bill5 = din // 5000
                                din = din - (5000 * bill5)
                        else:
                            if din >= 10000:
                                bill10 = din // 10000
                                din = din - (10000 * bill10)
                                if din >= 5000:
                                    bill5 = din // 5000
                                    din = din - (5000 * bill5)
                            else:
                                bill5 = din // 5000
                                din = din - (5000 * bill5)
                        billetes20 = billeste20 - bill20
                        billetes10 = billetes10 - bill10
                        billetes5 = billetes5 - bill5
                        print("billetes 20000=", bill20)
                        print("bilettes 10000=", bill10)
                        print("billetes 5000=", bill5)
                        print("saldo cuenta=", saldo, ",", "saldo cajero=", monto_cajero)
                        res = input("¿Desea retirar más dinero?",)
                break
            break
        else:
            print("Clave invalida")
    if intentos >= 3:
        print("Tarjeta bloqueada")
else:
    print("Usuario invalido")

print("Finalizo su sesión")