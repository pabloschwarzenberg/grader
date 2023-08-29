#Cajero Automático
# Saldos iniciales
saldo_cajero=1000000
saldo_cuenta=100000
x=0
seguir="n"
print("Bienvenido")
import sys
while(seguir=="n"):
    # Ingreso de usuario
    usuario=int(input("Ingrese usuario: "))
    # Ingreso clave
    clave=int(input("Ingrese su clave: "))
    while(x<2) and (clave!=1803):
        print("Clave invalida")
        x=x+1
        clave=int(input("Ingrese su clave: "))       
    if(clave==1803):
        #Ingreso de monto
        monto=int(input("Ingrese monto a retirar: "))
        if(monto<=saldo_cuenta):
            # Actualizacion de saldos
            saldo_cuenta=saldo_cuenta-monto
            saldo_cajero=saldo_cajero-monto
            print("Saldo cuenta=",saldo_cuenta)
            print("Saldo cajero=",saldo_cajero)
        else:
            print("Monto no permitido")
    else:
        print("Tarjeta bloqueada")
        sys.exit()
    # Repeticion de programa
    seguir=input("¿Desea realizar otra operación?: ")