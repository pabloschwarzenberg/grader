#Cajero Automático
cont = 0
while True:
    numero = 10334151
    SIC = 1000000
    billetes = (20000, 10000, 5000)
    cant = (20, 40, 40)
    saldo_cuenta = 100000
    usuario = int(input("Ingrese su usuario: "))
    if usuario == numero:
        clave = int(input("Ingrese su clave: "))
        if clave == 1803:
            print("Su saldo de cuenta es 100000")
            retiro = int(input("cuanto dinero quiere retirar? "))
            if retiro > saldo_cuenta:
                print("monto no permitido")
                break
            if retiro < SIC:
                print("saldo cuenta =", saldo_cuenta-retiro)
                print("saldo cajero =", SIC-retiro)
                print("billetes 20000 =", round(retiro // billetes[0]))
                retiro = retiro - 20000*round(retiro // billetes[0])
                print("billetes 10000 =", round(retiro // billetes[1]))
                retiro = retiro - 10000 * round(retiro // billetes[1])
                print("billetes 5000 =", round(retiro // billetes[2]))
                retiro = retiro - 5000 * round(retiro // billetes[2])
            break
        if clave != 1803:
            print("clave invalida")
            cont = cont + 1
        if cont == 3:
            print("tarjeta bloqueada")
            break
