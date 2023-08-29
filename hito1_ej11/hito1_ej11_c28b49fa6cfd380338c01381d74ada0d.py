#Cajero Automático
ide=int(input("ingresa el usuario"))
clave=int(input("ingrese su clave:"))
intentos=1
saldo_c=1000000
saldo_u=100000
user=10334151
contra=1803
billetes_20=20000
billetes_10=10000
billetes_5=5000

def bills(c,x):
    billetes=c//x
    resto=c % x
    return billetes,resto
while clave !=contra:
    intentos += 1
    if clave==contra:
        print("clave incorrecta")
        break
    if intentos> 3:
        break
    print("clave invalida")
    clave=int(input("ingrese de nuevo su clave"))

if intentos>3:
    print("tarjeta bloqueada")
if ide== user:
    if clave==contra:
        monto=int(input("¿cuanto desea retirar?:"))

        if monto>saldo_u and monto> saldo_c:
            print("monto no permitido")

        else:
            saldo_u -=monto
            saldo_c-=monto
            b,r=bills(monto,billetes_20)
            c,r=bills(r,billetes_10)
            j,r=bills(r,billetes_5)
            print("saldo cuenta="+str(saldo_u))
            print("saldo cajero="+str(saldo_c))
            print("billetes 20000="+str(b))
            print("billetes 10000="+str(c))
            print("billetes 5000="+str(j))     