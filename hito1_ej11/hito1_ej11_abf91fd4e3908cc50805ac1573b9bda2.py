#Cajero Automático
import time

print("Bienvenido al cajero automatico del Banco de Pelotillehue")

rut=int(input("Por favor ingrese su rut sin puntos ni guión: "))

#Para Salir
Salir=0
#Lista de Variables de ingreso:
ClaveCorrecta=0
Fallos=0
#Lista de Variables el cajero:
DineroCajero=1000000
d=0
#Lista dinero de Claudio:
DineroClaudio=100000
#Cantidad de Billetes:
CVeinte=20
CDiez=40
CCinco=40
A=0
B=0
C=0

while ClaveCorrecta==0:

    clave = int(input("Ingrese su clave super secreta: "))

    if rut==10334151 and clave==1803:

        print("Clave Aprobada")

        ClaveCorrecta=1


    if rut==10334151 and clave!=1803:

        print("clave invalida")

        Fallos+=1

    if Fallos==3:

        print("tarjeta bloqueada")

        ClaveCorrecta=-1

if ClaveCorrecta==1:

    print("Ingresando")

    time.sleep(2)

    print("Listo")

    time.sleep(1)

while ClaveCorrecta==1:

    DineroRetirar=int(input("Ingresar Dinero a retirar: "))

    if DineroRetirar%5000!=0:

        print("Por favor solicitar monto multiplo de 5000")

    if DineroRetirar <= DineroClaudio and DineroRetirar%5000==0:

        DineroClaudio=DineroClaudio-DineroRetirar
        DineroCajero=DineroCajero-DineroRetirar

        d = DineroRetirar

        Veinte = DineroRetirar // 20000

        while d >= 20000 and CVeinte > 0:
            d = d - 20000
            A+=1
            CVeinte-=1

        Diez = d // 10000

        while d >= 10000 and CDiez > 0:
            d = d - 10000
            B+=1
            CDiez-=1

        Cinco = d // 5000

        while d >= 5000 and CCinco > 0:
            d = d - 5000
            C+=1
            CCinco-=1

        time.sleep(5)

        print("Retire su dinero.")
        print("Billetes 20000=",A)
        print("Billetes 10000=", B)
        print("Billetes 5000=", C)
        print("saldo cuenta=",DineroClaudio)
        print("saldo cajero=",DineroCajero)

    DineroRetirar = 0

    if (DineroClaudio < DineroRetirar) or (DineroCajero < DineroRetirar):

        print("monto no permitido")

    Salir=input("Ingrese N para continuar")

    if Salir != "N":

        ClaveCorrecta=2




      