def identificar(clave):
    intentos=1
    while intentos<3:
        if clave!=1803:
            intentos=intentos+1
            clave=int(input("clave: "))
            if intentos ==3:
                return False            
        return True
def montoaretirar():
    retirar=int(input("cuanto quiere retirar: "))
    while retirar>=platacuenta and retirar>=platacajero:
        print ("monto no permitido")
        retirar=int(input("cuanto quiere retirar: "))
    return retirar
def billetes (t):
    x=retirar%20000
    c=(retirar-x)/20000
    c=int(c)
    y=x%10000
    u=(x-y)/10000
    u=int(u)
    z=y%5000
    q=(y-z)/5000
    q=int(q)
    return print("billetes 20000=",c),print("billetes 10000=",u),print("billetes 5000=",q)
platacuenta=100000
platacajero=1000000
while (True):
    usuario=int(input("usuario: "))
    clave=int(input("clave: "))
    terminar="N"
    if identificar(clave)==False:
        print("tarjeta bloqueada")
        break;
    retirar=0
    retirar= montoaretirar()
    platacajero=platacajero-retirar
    platacuenta=platacuenta-retirar
    print ("saldo cuenta=",platacuenta)
    print ("saldo cajero=",platacajero)
    billetes(retirar)
    terminar=str(input("para salir presione algo distinto a la letra “N”: "))
    if (terminar!="N") and (terminar!="n"):
        break;