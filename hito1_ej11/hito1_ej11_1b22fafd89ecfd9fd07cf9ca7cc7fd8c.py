#Cajero Automático
cuenta_bancaria = eval(input("Ingrese cuenta:"))
clave = ""
intentos = 3
saldo_cajero = 1000000
saldo_cuenta = 100000
retiro = ""
de_20 = 20
de_10 = 40
de_5 = 40
if(cuenta_bancaria == 10334151):
    while(clave == ""):
        clave = eval(input("ingrese clave:"))
        if(clave != 1803):
            intentos = intentos-1
            print("clave incorrecta, le quedan", intentos, "intento(s)")
            clave = ""
            if(intentos == 0):
                print("tarjeta bloqueada")
                clave = "tarjetabloqueada"
        if(clave == 1803):
            while(retiro == ""):
                retiro = eval(input("Ingrese monto a retirar:"))
                if(retiro > saldo_cuenta):
                    print("monto no permitido")
                    retiro = ""
            if(retiro < saldo_cuenta):
                de_20 = retiro//20000
                de_10 = (retiro%20000)//10000
                de_5 = ((retiro%20000)%10000)//5000
                print("saldo cuenta=", saldo_cuenta-retiro)
                print("saldo cajero=", saldo_cajero-retiro)
                print("billetes 20000=", de_20)
                print("billetes 10000=", de_10)
                print("billetes 5000=", de_5)
                
    if(clave == "tarjeta bloqueada"):
        print()    