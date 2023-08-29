#Cajero Automático
u = int(input("Ingrese el usuario: "))
cont = int(input("Ingrese su clave: "))
intentos = 1
sc = 1000000
su = 100000
user = 10334151
contra = 1803
billetes_20 = 20000
billetes_10 = 10000
billetes_5 = 5000


def bills(c, x):
    billetes = c // x
    resto = c % x
    return billetes, resto


while cont != contra:
    intentos += 1
    if cont == contra:
        print("clave incorrecta")
        break
    if intentos > 3:
        break
    print("clave invalida")
    cont = int(input("Ingrese de nuevo su clave: "))

if intentos > 3:
    print("tarjeta bloqueada")

if u == user:
    if cont == contra:
        monto = int(input("¿Cuanto quiere retirar?: "))
        if monto > su and monto > sc:
            print("monto no perimitido")
        else:
            su -= monto
            sc -= monto
            b, r = bills(monto, billetes_20)
            c, r = bills(r, billetes_10)
            j, r = bills(r, billetes_5)
            print("saldo cuenta=" + str(su))
            print("saldo cajero=" + str(sc))
            print("billetes20000=" + str(b))
            print("billetes10000=" + str(c))
            print("billetes5000=" + str(j))  