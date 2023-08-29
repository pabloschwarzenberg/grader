billetes = [20000,10000,5000] #Los tipos de billetes que exixten
user = [10334151, 1803, 100000] #Datos del usuario válido y registrado. Usuario, clave y saldo en su cuenta
cajero = [20,40,40, 1000000]  #Datos del Cajero Automático. Candidad de billetes por tipo de billete y el saldo

usuario =int(input("Ingrese su usuario: "))
#usuario = 10334151
while not (usuario == user[0]):
    usuario = int(input("ingrese nuevamente su usuario: "))

clave = int(input("Ingrese su clave: "))
#clave = 1803
intentos = 1
while clave != user[1] and intentos<3:
    intentos = intentos + 1
    clave = int(input("Clave invalida, Reintente: "))

if intentos == 3:
    print("Clave bloqueada")
else:
    montoaRetirar = int(input("Ingrese monto a retirar: "))
    if montoaRetirar >= cajero[3] or montoaRetirar >= user[2]:
        print("Monto no permitido")
    else:
        user[2] =  user[2] - montoaRetirar
        cajero[3] = cajero[3] - montoaRetirar
        print("saldo cuenta=",user[2])
        print("saldo cajero=",cajero[3])
        saldo = montoaRetirar
        salidaBilletes = [0,0,0]
        while saldo>0:
            if saldo>= billetes[0]:
                saldo = saldo - billetes[0]
                salidaBilletes[0]= salidaBilletes[0]+1
            if saldo>= billetes[1]:
                saldo = saldo - billetes[1]
                salidaBilletes[1]= salidaBilletes[1]+1
            if saldo>= billetes[2]:
                saldo = saldo - billetes[2]
                salidaBilletes[2]= salidaBilletes[2]+1
        print("billetes", billetes[0],"=", salidaBilletes[0])
        print("billetes", billetes[1],"=", salidaBilletes[1])
        print("billetes", billetes[2],"=", salidaBilletes[2])
