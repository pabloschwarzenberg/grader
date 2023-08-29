#Cajero Automático

usuario=10334151
clave=1803
saldo_maquina=1000000
saldo_cuenta=100000
clave_ingresada=input()
while clave_ingresada!=clave:
    print("clave invalida")
    clave_ingresada = input()
if clave_ingresada==clave:
    monto=int(input()):
    if monto<100000:
        saldo_cuenta=saldo_cuenta-monto
        saldo_maquina=saldo_maquina-monto
        print(saldo_cuenta)
        print(saldo_maquina)
    else:
        print("monto no permitido")      