
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

#BLOQUE PRINCIPAL:
saldoCajero = 1000000
usuario = 10334151
clave = 1803
saldoCuenta = 100000
cont = 0
nbT20000 = 20
nbT10000 = 40
nbT5000 = 40
while True:
    pw = clave
    bloqueo = True
    while bloqueo and cont < 3:
        #us = int(input("Ingresa rut: "))
        pw = int(input("Ingresa clave: "))
        if pw != clave:
            print("clave invalida")
            cont += 1
            if cont == 3:
                bloqueo = False
        else:
            cont = 3
    if bloqueo == False:
        print("tarjeta bloqueada")
        break
    retiro = int(input("qué monto quieres retirar? "))
    if retiro > saldoCuenta or retiro > saldoCajero:
        print("monto no permitido")
    else:
        saldoCuenta -= retiro
        saldoCajero -= retiro
        print("saldo cuenta="+str(saldoCuenta))
        print("saldo cajero="+str(saldoCajero))
        ListaBilletes = nbEntregados(retiro)
        nbT20000 = nbT20000 - ListaBilletes[0]
        nbT10000 = nbT10000 - ListaBilletes[1]
        nbT5000 = nbT5000 - ListaBilletes[2]        
        print("billetes 20000=" + str(ListaBilletes[0]))
        print("billetes 10000=" + str(ListaBilletes[1]))
        print("billetes 5000=" + str(ListaBilletes[2]))        
    op = input("Deseas salir? ")
    if op != "N":
        break
      