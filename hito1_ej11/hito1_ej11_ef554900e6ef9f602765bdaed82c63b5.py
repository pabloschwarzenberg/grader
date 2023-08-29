#Cajero Automático
# Saldos iniciales billetes
billetes_de_20=20
billetes_de_10=40
billetes_de_5=40
# Saldos iniciales generales
saldocajero=20000*billetes_de_20+10000*billetes_de_10+5000*billetes_de_5
saldocuenta=100000
x=0
seguir="n"
import sys
print("Bienvenido")
while(seguir=="n"):
    # Ingreso de usuario
    usuario=input("Ingrese su usuario: ")
    # Ingreso clave
    clave=int(input("Ingrese su clave: "))
    while(x<2) and (clave!=1803):
        print("Clave invalida")
        x=x+1
        clave=int(input("Ingrese su clave: "))       
    if(clave==1803):
        #Ingreso de monto
        monto=int(input("Ingrese monto a retirar: "))
        if(monto<=saldocuenta):
            # Actualizacion de saldos
            saldocuenta=saldocuenta-monto
            saldocajero=saldocajero-monto
            billetes_entregados_de_20=monto//20000
            billetes_entregados_de_10=(monto%20000)//10000
            billetes_entregados_de_5=((monto%20000)%10000)//5000
            billetes_de_20=billetes_de_20-billetes_entregados_de_20
            billetes_de_10=billetes_de_10-billetes_entregados_de_10
            billetes_de_5=billetes_de_5-billetes_entregados_de_5
            print("Saldo cuenta=",saldocuenta)
            print("Saldo cajero=",saldocajero)
            print("Billetes 20000=",billetes_entregados_de_20)
            print("Billetes 10000=",billetes_entregados_de_10)
            print("Billetes 5000=",billetes_entregados_de_5)
        else:
            print("Monto no permitido")
    else:
        print("Tarjeta bloqueada")
        sys.exit("Gracias por preferirnos, vuelva pronto")
    # Repeticion de programa
    seguir=input("¿Desea realizar otra operación?: ")

