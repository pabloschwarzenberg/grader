#Cajero Automático
plata_cajero=1000000
plata=100000
r="N"
clave=0
intentos=3
usuario=int(input())
if usuario==10334151:
    while intentos>0:
        clave=int(input())
        if clave==1803:
            break
        else:
            print("clave invalida")
            intentos-=1
    if clave==1803:
        while r=="N":
            while plata_cajero>0:
                monto=int(input())
                if plata - monto > 0:
                    plata-=monto
                    plata_cajero-=monto
                    if plata>0:
                        print("saldo cuenta=",plata)
                        print("saldo cajero=",plata_cajero)
                        break
                else:
                    print("monto no permitido")
                    break
            r=input()
    else:
        print("trarjeta bloqueada")
else:
    print("usuario invalido")