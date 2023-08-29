#Cajero Automático
s_cajero=1000000
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
            break
        else:
            print ("monto no permitido")