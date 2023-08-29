#Cajero Automático

import sys

usuario = int(input("Ingrese numero de usuario: "))

while usuario != 10334151:
    print("Ingrese el usuario correcto")
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
cuenta = 10000
retirar = int(input("Monto a retirar: "))

while (inicial > -1) and (retirar <= inicial):
    cuenta = cuenta + retirar
    inicial = inicial - retirar
    print("saldo cuenta=",cuenta)
    print("saldo cajero=",inicial)
    pregunta = input("presione la tecla 'N' para seguir")
    
    if pregunta == "N":
        retirar = int(input("Monto a retirar: "))
        
    elif pregunta != "N":
        break
    
    elif retirar > inicial:
        print("monto no permitido")
        retirar = int(input("Monto a retirar: "))
        