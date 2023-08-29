#Cajero Automático
saldo_cajero = 1000000
n_20000 = 20
n_10000 = 40
n_5000 = 40
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
            if monto_ret%5000 == 0:
                b_ent_20000 = monto_ret//20000
                b_ent_10000 = (monto_ret%20000)//10000
                b_ent_5000 = ((monto_ret%20000)%10000)//5000
                saldo_usuario -= monto_ret
                saldo_cajero -= monto_ret
                print("Billetes 20000 =",b_ent_20000)
                print("Billetes 10000 =",b_ent_10000)
                print("Billetes 5000 =",b_ent_5000)
                print("Saldo cuenta =", saldo_usuario)
                print("Saldo cajero =", saldo_cajero)
            else:
                print("Monto debe ser múltiplo de 5000")
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