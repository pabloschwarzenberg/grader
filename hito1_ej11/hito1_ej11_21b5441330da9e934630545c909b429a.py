#Cajero Automático
from random import randint
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

def nbEntregados(monto):
    
    nb20000 = 0
    nb10000 = 0
    nb5000 = 0
    
    while monto>0:
        if monto >= 20000:
            
            nb20000 = nb20000 + 1
            monto = monto - 20000
            
        elif monto >= 10000:
            
            nb10000 = nb10000 + 1
            monto = monto - 10000
            
        elif monto >= 5000:
            
            nb5000 = nb5000 + 1
            monto = monto - 5000
            
    return [nb20000, nb10000, nb5000]

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
            L = nbEntregados(monto)
            print("billetes 20000=" + str(L[0]))
            print("billetes 10000=" + str(L[1]))
            print("billetes 5000=" + str(L[2]))
            intento = intento + 5

        elif opcion == invalida:
            print("clave invalida")
            intento = intento + 1

    if intento == 4:
        print("tarjeta bloqueada")
##PROGRAMA
User()