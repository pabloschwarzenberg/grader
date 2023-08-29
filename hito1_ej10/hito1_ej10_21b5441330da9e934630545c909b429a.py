#Cajero Automático
MontoInicialCajero = 1000000
correcto = 1
invalida = 2
intento = 1
##FUNCIONES
def usuario_(InUsuario, InClave):
    usuario = 10334151
    clave =1803
    if usuario==InUsuario and clave==InClave:
        return 1
    else:
        return 2

def SaldoUser(MontoRe):
    saldo = 100000
    saldo = 100000 - MontoRe
    return saldo

def SaldoCaj(monto):
    saldo = 1000000
    monto = monto
    while monto>100000:
        print("monto invalido")
        monto = int(input("monto retirar: "))

    saldo = 1000000 - monto
    return saldo

def User():
    intento = 1
    while intento <=3:
        usuario =int(input("Usuario: "))
        clave = int(input("Clave: "))
        opcion = usuario_(usuario,clave)
        if opcion == correcto:
            monto = int(input("monto retirar: "))
            print("saldo cuenta="+str(SaldoUser(monto)))
            print("saldo cajero="+str(SaldoCaj(monto)))
            intento = intento + 5

        elif opcion == invalida:
            print("clave invalida")
            intento = intento + 1

    if intento == 4:
        print("tarjeta bloqueada")
##PROGRAMA
User()