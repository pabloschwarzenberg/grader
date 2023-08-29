def pedirClave(a):
    p = int(input(a))
    return p
def login(r, p):
    saldo = 0
    block = False
    intentos = 0
    if ru == 10334151:
        while block == False:
            if p == 1803:
                saldo = 100000
                opcion='s'
                break
            else:
                if intentos == 3:
                    print("tarjeta bloqueada")
                    opcion = 'n'
                    block = True
                else:
                    clave = pedirClave("clave invalida")
                    intentos = intentos + 1
    else:
        saldo = 1000000
        opcion = 's'
    return saldo, opcion
def modSaldo(s, sc):
    retiro=int(input("Ingrese el monto que desea retirar: "))
    if retiro>s:
        print("monto no permitido")
    else:
        s= s-retiro
        sc= sc -retiro
    return s, sc
saldCajero=1000000
opc=''
while opc !='n':
    ru= int(input("Ingrese su rut: "))
    clave= int(input("Ingrese su Clave: "))
    sald,opc=login(ru,clave)
    sald,saldCajero=modSaldo(sald,saldCajero)
    print("saldo cuenta=", sald)
    print("saldo cajero=", saldCajero)
    opc=input("Desea continuar s/n")