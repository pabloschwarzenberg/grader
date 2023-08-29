saldo_cajero = 1000000
USUARIO = 10334151
CLAVE = 1803
saldo_usuario = 100000
n = 0
while True:
    usuario_ingre = int(input("Ingrese usuario: "))
    clave_ingre = int(input("Ingrese clave: "))
    if clave_ingre == CLAVE:
        monto_ret = int(input("Monto a retirar: "))
        if monto_ret>saldo_usuario:
            print("Monto no permitido")
        else:
            saldo_usuario -= monto_ret
            saldo_cajero -= monto_ret
            print("Saldo cuenta=", saldo_usuario)
            print("Saldo cajero=", saldo_cajero)
    else:
        print("Clave inválida")
        n += 1
        if n==3:
            print("Tarjeta bloqueada")
            break
    print("Para salir ingrese letra distinta a N: ")
    print("Para continuar ingrese letra N: ")
    letra = input()
    if letra !='N':
        break