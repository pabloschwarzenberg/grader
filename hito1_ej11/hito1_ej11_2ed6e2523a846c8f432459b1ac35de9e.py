#Cajero Automático
s_cajero=1000000
veinte=20
diez=40
cinco=40
usuario=10334151
clave=1803
s_cuenta = 100000
intentos=0
usu = int(input("Ingrese usuario:"))
while not (usu == usuario):
    usu = int(input("Ingrese usuario:"))
while True:
    key = int(input("Ingrese clave:"))
    if key != 1803:
        print("clave invalida")
        intentos = intentos + 1
        if intentos == 3:
            print("tarjeta bloqueada")
            break
    else:
        monto = int(input("Ingrese monto:"))
        if monto <= s_cuenta:
            s_cuenta = s_cuenta - monto
            s_cajero = s_cajero - monto
            print ("saldo cuenta=",s_cuenta)
            print ("saldo cajero=",s_cajero)
            total=0
            saldo=0
            while not (total == monto):
                t20 = int(monto/20000)
                saldo=monto-(t20*20000)
                t10 = int(saldo/10000)
                saldo=monto-((t20*20000)+(t10*10000))
                t5 = int(saldo/5000)
                total=(t20*20000)+(t10*10000)+(t5*5000)
                print("billetes 20000=",t20)
                print("billetes 10000=",t10)
                print("billetes 5000=",t5)
            break
        else:
            print ("monto no permitido")
