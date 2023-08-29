#Cajero Automático
import sys
saldoc=1000000
saldou=100000
intentos=3
Estado=False
B20=20
B10=40
B5=40
billetes20000=0
billetes10000=0
billetes5000=0
montoinvalido=True
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
 while montoinvalido==True:
    md=int(input("Ingrese el monto deseado"))
    while md>saldou:
        print("Ud. No posee esa cantidad de money, por favor ingresa otro monto")
        md=int(input("Ingrese el monto deseado"))
    if md<=saldou and md%5000==0:
     montoinvalido=False
     saldoc=saldoc-md
     saldou=saldou-md
     while 0<=md-20000:
              md=md-20000
              B20=B20-1
              billetes20000=billetes20000+1
     while 0<=md-10000:
              md=md-10000
              B10=B10-1
              billetes10000=billetes10000+1
     while 0<=md-5000:
              md=md-5000
              B5=B5-1
              billetes5000=billetes5000+1
     print("Retire su money")
     print("saldo cuenta=",saldou,"saldo cajero=",saldoc)
     print("Billetes 20000=",billetes20000)
     print("Billetes 10000=",billetes10000)
     print("Billetes 5000=",billetes5000)
    else:
        print("Monto Invàlido")
     
    
 