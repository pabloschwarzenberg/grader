#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
intentos=0
while intentos < 3:
    usuario=int(input("Ingresar usuario: "))
    if usuario==10334151:
        clave=int(input("Ingresar clave: "))
        intentos += 1
        if clave == 1803:
            print(clave)
            monto=input("Ingresar monto a retirar: ")
            monto=int(monto)
            saldo_cajero=saldo_cajero-monto
            saldo_cuenta=saldo_cuenta-monto
            print("Saldo cuenta=",saldo_cuenta)
            print("Saldo cajero=",saldo_cajero)
            print("Retire su tarjeta")
            break
        else:
         print("clave inválida")

if intentos>=3:
    print("Tarjeta bloqueada")  