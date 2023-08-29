user=10334151
clave=1803
saldo=100000
saldocajero=1000000
userinp=int(input("Ingresar usuario: "))
claveinp=int(input("Ingresar clave: "))
correcto=0
while correcto!=5:
    if claveinp!=clave:
        print("Clave inválida")
        claveinp=int(input("Ingresar clave: "))
        correcto=correcto+1
    if correcto==2:
        print("Tarjeta bloqueada")
        quit()
    if claveinp==clave:
        correcto=5
if claveinp==clave:
    correcto=5
    monto=int(input("Ingrese el monto a retirar"))
    if monto not in range (1, saldo) or monto not in range (1,saldocajero):
        print("monto no permitido")
    else:
        saldo=saldo-monto
        saldocajero=saldocajero-monto
        print("saldo cuenta=", saldo)
        print("saldo cajero=", saldocajero)
