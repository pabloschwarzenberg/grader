saldo_cajero = 1000000
saldo_cuenta = 100000

def run():
    global saldo_cajero
    global saldo_cuenta
    while(True):
        try:
            monto = int(input("Monto a retirar: "))
        except EOFError:
            monto = 0
        if(monto > saldo_cuenta):
            print("monto no permitido")
        else:
            saldo_cuenta = saldo_cuenta - monto
            saldo_cajero = saldo_cajero - monto
            print("saldo cuenta=%d" %saldo_cuenta)
            print("saldo cajero=%d" %saldo_cajero)
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
