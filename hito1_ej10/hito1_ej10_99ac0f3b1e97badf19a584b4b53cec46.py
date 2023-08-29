#Cajero Automático
cuenta_cajero = eval(input("Ingrese cuenta:"))
clave_cajero = ""
intentos=3
saldo_cajero=1000000
saldo_cuenta=100000
retiro=""
if(cuenta_cajero==10334151):
    while(clave_cajero==""):
        clave_cajero = eval(input("ingrese clave:"))
        if(clave_cajero!=1803):
            intentos=intentos-1
            print("clave incorrecta, le quedan", intentos, "intento(s)")
            clave_cajero=""
            if(intentos==0):
                print("tarjeta bloqueada")
                clave_cajero="tarjetabloqueada"
        if(clave_cajero==1803):
            while(retiro==""):
                retiro = eval(input("Ingrese monto a retirar:"))
                if(retiro > saldo_cuenta):
                    print("monto no permitido")
                    retiro=""
            if(retiro < saldo_cuenta):
                print("saldo cuenta=", saldo_cuenta-retiro)
                print("saldo cajero=", saldo_cajero-retiro)
                
    if(clave_cajero=="tarjeta bloqueada"):
        print()     