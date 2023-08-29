# raise NameError('{0}'.format(clave))

respuesta="N"
n=0
saldo=10**5
saldo_cajero=10**6
while respuesta=="N":
    while n<3:
        usuario = int(input("usuario: "))
        clave = int(input("contraseña: "))
        if usuario==10334151 and clave==1803:
            n=n+10
            # break
        else:
            print("clave invalida")
            n=n+1
    if n==3:
        print("tarjeta bloqueada")
        respuesta=str("N1")
    if n!=3:
        monto_retirar = int(input("monto deseado: "))
        
        if monto_retirar>saldo:
            print("monto invalido")
            respuesta=input("quiere realizar otra operacion? ")
          
        else:
            saldo=saldo-monto_retirar
            saldo_cajero=saldo_cajero-monto_retirar
            print("saldo cuenta={0}".format(saldo))
            print("saldo cajero={0}".format(saldo_cajero))
            respuesta=input()

        