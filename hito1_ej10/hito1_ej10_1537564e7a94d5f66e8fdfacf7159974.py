usuario=int(input("ingrese n° usuario:"))
i=0
clave=int(input("Ingrese contraseña:")) 


if clave==1803:     #Cuando contraseña es correcta
    z=int(input("Ingrese monto a retirar:"))
    if z>100000:
        print("Monto NO permitido")
    elif z<=100000:
        print("Saldo cuenta="+str(100000-z),"\nSaldo Cajero="+str(1000000-z))


if clave!=1803:
    while i<=3:           #cuando contraseña es Incorrecta
        if clave!=1803 and i==0:
            print("Clave Inválida")
        elif clave!=1803 and 0<i<3:
            clave=int(input("Ingrese contraseña:"))
            print("Clave Inválida")
        elif clave!=1803 and i==3:
            print("Tarjeta Bloqueada")
        elif clave==1803:
            z=int(input("Ingrese monto a retirar:"))
            if z>100000:
                print("Monto NO permitido")
            elif z<=100000:
                print("Saldo cuenta="+str(100000-z),"\nSaldo Cajero="+str(1000000-z))
        i+=1



      