#Cajero Automático

#Variables
saldo_cajero = 1000000
saldo_cuenta = 100000
intentos = 0

#Proceso
try:
    while intentos < 3:
        usuario = input("Ingrese su usuario: ")
        clave = int(input("Ingrese su clave: "))
        usuario = int(usuario)
        clave = int(clave)
        if usuario == 10334151 and clave == 1803:
            retiro = int(input("¿Cuánto dinero desea retirar?"))
            if retiro > saldo_cuenta:
                print("monto no permitido")
            else:
                saldo_cuenta = (saldo_cuenta - retiro)
                saldo_cajero = (saldo_cajero - retiro)

                saldo_cuenta = str(saldo_cuenta)
                saldo_cajero = str(saldo_cajero)

                print("saldo cuenta="+saldo_cuenta)
                print("saldo cajero="+saldo_cajero)
        else:
            print("clave invalida")
            intentos = intentos + 1
        
    else:
        print("tarjeta bloqueada")
except EOFError:
    print("Error")

