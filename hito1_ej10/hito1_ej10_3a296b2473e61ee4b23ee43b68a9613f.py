#Cajero Automático
def Monto(monto,usuario=100000,cajero=1000000):
    if monto<=cajero:
        cajero = cajero-monto
        usuario = usuario-monto
        print("saldo cajero=",cajero)
        print("saldo cuenta=",usuario)
        respuesta1= [usuario,cajero]
        return respuesta1
    if monto > cajero:
        respuesta2= "monto no permitido"
        return respuesta2

variable1 = 0
variable2 = 0
intentos = 0
while variable2 == 0:
    if variable1 == 0:
        print("Usuario")
        input()
        print("clave")
        clave = input()
        if clave == "1803":
            variable1 = 1
        elif intentos == 2:
            print("Tarjeta bloqueada")
            break
        else:
            intentos += 1
    elif variable1 == 1:
        print("Ingrese monto a retirar")
        ingrese = input()
        letrasquenovan = "abcdefghijklmñopqrstuvwxyz,.-{}+´¿ABCDEFGHIJKLMÑOPQRSTUVWXYZ"
        if ingrese in letrasquenovan:
            break
        elif ingrese == "N":
            variable1 = 1
        else:
            Monto(float(ingrese))