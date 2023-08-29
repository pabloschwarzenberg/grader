#Cajero Automático
intentos=0
saldocajero=1000000
saldocuenta=100000
retiro = 0
while intentos<3:
    user=input("Ingrese Codigo de usuario:")
    clave=input("Ingrese clave numerica")
    if clave==" " or len(clave)<4 or len(clave)>4 :
        print("Clave invalida")
        intentos+=1
    else:
        pass
    while retiro ==0:
        retiro=int(input("Monto a retirar"))
        if retiro > saldocuenta:
            print("Monto no permitido")
            retiro=0
        elif retiro> saldocajero:
            print("Monto no permitido")
            retiro=0
        saldocajero=saldocajero-retiro
        saldocuenta=saldocuenta-retiro
        print("saldo cuenta=",saldocuenta)
        print("saldo cajero=",saldocajero)
    break
if intentos==3:
    print("Tarjeta bloqueada")


cantidad = retiro

cant5 = cantidad // 20000
resto5 = cantidad % 20000

cant2 = resto5 // 10000
resto2 = resto5 % 10000

cant1 = resto2 // 5000
resto1 = resto2 % 5000

print(" billetes 20000=", cant5)
print(" billetes 10000=", cant2)
print(" billetes 5000=", cant1)