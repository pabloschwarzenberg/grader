#Cajero Automático
def monto(monto,cajero=1000000,usuario=100000):
    if monto > cajero:
        print("Monto no permitido")
    else:
        usuario = usuario - monto
        cajero = cajero - monto
        print("saldo cuenta=",usuario)
        print("saldo cajero=",cajero)


usuario = 0
clave = 0
intentos = 0

while usuario == 0:
    if clave == 0:
        Usuario = input("Ingrese Usuario: ")
        Clave = input("Ingrese Clave: ")
        if Clave == "1803":
            clave = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos = intentos + 1
    elif clave == 1:
        monto_a_retirar = input("Ingrese el monto a retirar: ")
        salir = "ASDFGHJKL;QWERTYUIO;qwertyu"
        if monto_a_retirar in salir:
            break
        elif monto_a_retirar == "N":
            clave = 1
        else:
            monto(int(monto_a_retirar))  