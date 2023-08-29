#Cajero Automático
saldoCajero =1000000
billete20 =20
billete10 = 40
billete5 = 40
listavacia = []
usuario = 10334151
claveusuario = 1803
dineroUsuario = 100000
intento = 1
N = True
while N:
    if (billete20==0 and billete10==0 and billete5==0):
        print("cajero vacio")
        N = False
        break

    usuario = int(input("usuario :"))
    while intento<=3:
        clave = int(input("clave :"))
        if clave != claveusuario:
                print("clave invalidad")
                intento += 1
        elif clave == claveusuario:
                break

    if intento > 3:
        print("tarjeta bloqueada")
        N = False
        break
    
    denominaciones = [20000,10000,5000]
    print("monto a retirar ")
    monto = int(input("="))
    while monto>dineroUsuario or monto > saldoCajero:
        print("monto no permitido")
        monto = int(input("ingrese monto valido :"))
    else:
        saldoCajero -= monto
        dineroUsuario -= monto
        listavacia.append("saldo cuenta = "+str(dineroUsuario))
        listavacia.append("saldo cajero = "+str(saldoCajero))
        print(listavacia)
    Sumita = 0
    print (monto)
    for denominacion in denominaciones:
        cantidad = monto//denominacion
        if denominacion == 20000:
            if billete20 == 0:
                for i in range(len(denominaciones)):
                    if denominaciones[i]==20000:
                        denominaciones.pop(i)
            if  cantidad > billete20:
                cantidad = 20
            billete20 = billete20 - cantidad
            
        elif denominacion == 10000:
            if billete10 == 0:
                for i in range(len(denominacion)):
                    if denominaciones[i]==10000:
                        denominaciones.pop(i)
            if  cantidad > billete10:
                cantidad = 40
            billete10 = billete10-cantidad
        elif denominacion == 5000:
            if billete5 == 0:
                for i in range(len(denominacion)):
                    if denominaciones[i]==5000:
                        denominaciones.pop(i)
            if  cantidad > billete20:
                cantidad = cantidad - billete20
            billete5 = billete5 -(monto//denominacion)
        print ((cantidad),"Billetes de ", denominacion)
        monto = monto % denominacion
        Sumita += cantidad*denominacion
    

    continuar = input("presione N para realizar otra operacion")
    continuar = continuar.upper()
    if continuar != "N":
        N = False