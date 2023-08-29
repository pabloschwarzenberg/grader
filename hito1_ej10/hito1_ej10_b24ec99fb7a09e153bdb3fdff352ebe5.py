
usuario = 0
clave = 0
cajero = 1000000
cuenta = 100000
intentos = 0
monto = 0

if usuario == 0:
    usuario = int(input("Ingrese Usuario: "))
    if usuario == 10334151:
        clave = int(input("Ingrese clave: "))
        while intentos < 3:  
            if clave == 1803:
                monto = eval(input("Ingrese su monto a retirar: "))
                if monto > cuenta :
                    print("Monto no permitido")
                else:
                    cuenta = cuenta - monto
                    cajero = cajero - monto
                    print("Saldo Cuenta=",cuenta)
                    print("Saldo Cajero=",cajero)
                    break
            elif clave != 1803:                     
                print("CLave invalida")
                clave = int(input("Ingrese clave: "))
            intentos = intentos +1

        print("Tarjeta Bloqueada") 