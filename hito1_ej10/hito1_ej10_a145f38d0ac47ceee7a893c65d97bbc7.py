#Cajero Automático
cont = 0
while True:
    numero = 10334151
    usuario = int(input("Ingrese su usuario: "))
    if usuario == numero:
        clave = int(input("Ingrese su clave: "))
    SIC = 1000000
    saldo_cuenta = 100000
    if clave == 1803:
        print("Su saldo de cuenta es 100000")
        retiro = int(input("cuanto dinero quiere retirar? "))
        if retiro > saldo_cuenta:
            print("monto no permitido")
            break
        if retiro < SIC:
            print("saldo cuenta =",saldo_cuenta-retiro)

            print("saldo cajero =",SIC-retiro)
        break
    if clave != 1803:
        print("clave invalida")
        cont = cont + 1
    if cont == 3:
        print("tarjeta bloqueada")
        break
