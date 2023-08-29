billetes_20 = 20
billetes_10 = 40
billetes_5 = 40

saldo_cajero = 1000000
saldo_cuenta = 100000

def calculaBilletes(monto):
    veinte = int(monto / 20000)
    monto = monto - veinte*20000

    diez = int(monto / 10000)
    monto = monto - diez*10000

    cinco = int(monto / 5000)
    
    print("billetes 20000=%d" %veinte)
    print("billetes 10000=%d" %diez)
    print("billetes 5000=%d" %cinco)

def run():
    global saldo_cajero
    global saldo_cuenta
    while(True):
        try:
            monto = int(input("Monto a retirar: "))
        except EOFError:
            monto = 5
        if(monto > saldo_cuenta):
            print("monto no permitido")
        else:
            saldo_cuenta = saldo_cuenta - monto
            saldo_cajero = saldo_cajero - monto
            print("saldo cuenta=%d" %saldo_cuenta)
            print("saldo cajero=%d" %saldo_cajero)
            calculaBilletes(monto)
        try:
            continuar = input("Desea continuar?: ")
        except EOFError:
            continuar = 'N'
        if(continuar == 'N'):
            break

error = True
for i in range(3):
    username = int(input("Ingrese usuario: "))
    password = int(input("Ingrese password: "))
    if(username == 10334151 and password == 1803):
        run()
        error = False
        break

if(error):
    print("tarjeta bloqueada")

    





