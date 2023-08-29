#Cajero Automático
import sys
saldoc=1000000
saldou=100000
intentos=3
Estado=False
while(Estado==False and intentos>0):
    usuario=int(input("Ingrese su numero de usuario"))
    clave=int(input("Ingrese la clave"))
    if 10334151==usuario and clave==1803:
        Estado=True
        break
    else:
            print("Clave o usuario invalido, intente de nuevo")
            intentos=intentos-1
            print("Intentos restantes=",intentos)
if intentos==0:
                    print("Tarjeta bloqueada")
                    sys.exit()
if Estado==True:
    md=int(input("Ingrese el monto deseado"))
    
    while md>saldou:
        print("Ud. No posee esa cantidad de money, por favor ingresa otro monto")
        md=int(input("Ingrese el monto deseado"))
    if md<=saldou:
     print("Retire su money")
     saldoc=saldoc-md
     saldou=saldou-md
     print("saldo cuenta=",saldou,"saldo cajero=",saldoc)
     