#Cajero Automático
cuenta_bancaria= eval(input("Ingrese su cuenta bancaria:"))
clave = ""
intentos = 3
saldo_cajero = 1000000
saldo_cuenta = 100000
retiro = ""
if(cuenta_bancaria == 10334151):
    while(clave == ""):
        clave = eval(input("ingrese su clave:"))
        if(clave != 1803):
            intentos=intentos-1
            print("clave incorrecta, le quedan", intentos, "intento(s)")
            clave = ""
            if(intentos==0):
                print("tarjeta bloqueada")
                clave = "tarjetabloqueada"
        if(clave == 1803):
            while(retiro == ""):
                retiro = eval(input("Ingrese monto a retirar:"))
                if(retiro > saldo_cuenta):
                    print("monto no permitido")
                    retiro = ""
            if(retiro < saldo_cuenta):
                print("saldo cuenta=", saldo_cuenta-retiro)
                print("saldo cajero=", saldo_cajero-retiro)
                
    if(clave == "tarjeta bloqueada"):
        print()     