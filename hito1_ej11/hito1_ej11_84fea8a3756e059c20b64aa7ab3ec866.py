#Cajero Automático

import sys
import math

usuario = int(input("Ingrese numero de usuario: "))

while usuario != 10334151:
    print("Ingrese el usuraio correcto")
    usuario = int(input("Ingrese numero de usuario: "))

clave = int(input("Ingrese su clave: "))

intentos = 1

while intentos <= 2:
    if clave == 1803:
        print("Ha iniciado con exito")
        break
    
    if clave != 1803:
        print("clave invalida")
        clave = int(input("Ingrese su clave: "))
        intentos = intentos + 1

    if intentos > 2:
        print("tarjeta bloqueada")
        sys.exit()
        break
        
else:
    print("ERROR")
    input()
    
inicial = 1000000
cuenta = 100000
retirar = int(input("Monto a retirar: "))
retirarab = retirar

b20000 = retirar / 20000
b20000 = math.trunc(b20000)
retirar = retirar - (b20000 * 20000)
t20000 = 20 - b20000

b10000 = retirar / 10000
b10000 = math.trunc(b10000)
retirar = retirar - (b10000 * 10000)
t10000 = 40 - b10000

b5000 = retirar / 5000
b5000 = math.trunc(b5000)
retirar = retirar = retirar - (b5000 * 5000)
t5000 = 40 - b5000

while (inicial > -1) and (retirar <= inicial):
    cuenta = cuenta - retirarab
    inicial = inicial - retirarab

    print("saldo cuenta= ",cuenta)
    print("saldo cajero= ",inicial)
    print("billetes 20000=",b20000)
    print("billetes 10000=",b10000)
    print("billetes 5000=",b5000)
    pregunta = input("presione la tecla 'N' para seguir: ")
    
    if pregunta == "N":
        retirar = int(input("Monto a retirar: "))
        retirarab = retirar
        b20000 = retirar / 20000
        b20000 = math.trunc(b20000)
        retirar = retirar - (b20000 * 20000)
        t20000 = t20000 - b20000

        b10000 = retirar / 10000
        b10000 = math.trunc(b10000)
        retirar = retirar - (b10000 * 10000)
        t10000 = t10000 - b10000

        b5000 = retirar / 5000
        b5000 = math.trunc(b5000)
        retirar = retirar = retirar - (b5000 * 5000)
        t5000 = t5000 - b5000
        
    elif pregunta != "N":
        break
    
    elif retirar > inicial:
        print("monto no permitido")
        retirar = int(input("Monto a retirar: "))
        retirarab = retirar