#Cajero Automático
print("Inserte usuario")
u=int(input("Usuario="))
i=0
if u==10334151:
    while i<3:
        print("Inserte clave de 4 digitos")
        c=int(input("clave="))
        if c==1803:
            print("inserte monto a retirar")
            m = int(input("monto:"))
            if m > 100000:
                print("monto no permitido")
            elif m <= 100000 and m>0:
                scu=(100000-m)
                sca=(1000000-m)
                print("saldocuenta=",scu,",","saldocajero=",sca)
                break
        else:
            print("clave invalida")
            i=i+1
            if i==3:
                print("tarjeta bloqueda")
else:
    print("usuario incorrecto")