#Cajero Automático
saldocajero=1000000
x=100000
intentos=0
usuario=int(input("Ingrese su usuario:"))
clave=int(input("Ingrese su clave:"))
while usuario!=10334151 and clave!=1083:
    while intentos<=3:
        print("Clave incorrecta")
        usuario=int(input("Ingrese su usuario:"))
        clave=int(input("Ingrese su clave:"))
        intentos=intentos+1
        if intentos>=3:
            break

    print("La cuenta fue bloqueada.")
    break        

else:
    print("Bienvenido")
    print("Usted tiene un saldo de:", x)
    monto=int(input("Ingrese monto a retirar:"))
    print("Su saldo es:", x-monto)
    print("Saldo cajero:", saldocajero-monto)