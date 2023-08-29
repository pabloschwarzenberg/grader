#Cajero Automático
usuario = "10334151"
clave = "1803"
saldoca = 1000000
saldocu = 100000
usuarionew = input("ingrese su usuario: ")
clavenew = input("ingrese su clave: ")
n = "n"
while n == "n":
    cont = 1
    while cont < 3:
        if clavenew == clave:
            cont = 3
        else:
            print("clave invalida")
            clavenew = input("ingrese su clave: ")
        cont += 1
    if clavenew != clave:
        print("tarjeta bloqueada")
    else:
        monto = int(input("¿Cuanto desea retirar?: $"))
        while monto > saldocu:
                print("monto no permitido")
                monto = int(input("¿Cuanto desea retirar?: $"))
        newsaldoca = saldoca - monto
        newsaldocu = saldocu - monto
        print("Saldo Cuenta={}".format(newsaldocu))
        print("Saldo Cajero={}".format(newsaldoca))
    n = input()
