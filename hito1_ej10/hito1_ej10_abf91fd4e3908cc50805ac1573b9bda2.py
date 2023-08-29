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
#Lista dinero de Claudio:
DineroClaudio=100000

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

    if DineroRetirar <= DineroClaudio:

        DineroClaudio=DineroClaudio-DineroRetirar
        DineroCajero=DineroCajero-DineroRetirar

        print("Retirando dinero...")

        time.sleep(5)

        print("Retire su dinero.")
        print("saldo cuenta=",DineroClaudio)
        print("saldo cajero=",DineroCajero)

    DineroRetirar = 0

    if (DineroClaudio < DineroRetirar) or (DineroCajero < DineroRetirar):

        print("monto no permitido")

    Salir=input("Ingrese N para continuar")

    if Salir != "N":

        ClaveCorrecta=2