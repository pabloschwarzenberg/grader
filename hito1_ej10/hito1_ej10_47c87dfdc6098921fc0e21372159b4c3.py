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
    terminar=str(input("para salir presione algo distinto a la letra “N”: "))
    if (terminar!="N") and (terminar!="n"):
        break;