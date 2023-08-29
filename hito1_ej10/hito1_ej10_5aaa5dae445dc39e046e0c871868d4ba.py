#Cajero Automático
saldo_cajeroinicial=1000000
saldo_cuentainicial=100000
usuario=int(input("Ingrese su usuario: "))
while not usuario == 10334151:
    usuario=int(input("usuario invalido, ingrese nuevamente: "))

clave=int(input("Ingrese su clave: "))
contador_clave=0
while not clave ==1803:
    clave=int(input("clave invalida, intente nuevamente: "))
    contador_clave=contador_clave+1
    if contador_clave==3:
        print("tarjeta bloqueada")
        break
        
if contador_clave!=3:
    if clave==1803:
        monto_retirar=int(input("Monto a retirar: "))
        if monto_retirar>100000 and monto_retirar <0:
            print("monto no permitido")
        
        else:
            saldo_cajerofinal=saldo_cajeroinicial-monto_retirar
            saldo_cuentafinal=saldo_cuentainicial-monto_retirar
            print("Saldo cuenta=", saldo_cuentafinal)
            print("Saldo cajero=", saldo_cajerofinal)      