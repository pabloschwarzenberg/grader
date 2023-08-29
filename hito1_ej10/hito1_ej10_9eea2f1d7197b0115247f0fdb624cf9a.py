#Cajero Automático
usuario="10334151"
clave="1803"

def validar_clave(usuario_ingresado, clave_ingresada):
    if clave_ingresada==clave:
        monto=int(input("Ingrese el monto a retirar: "))
        cuenta=100000-monto
        cajero=1000000-monto
        print("saldo cuenta=", cuenta)
        print("saldo cajero=", cajero) 
        return True
    else:
        print("clave inválida")
        return False

intentos=3
while intentos>0:
    usuario_ingresado=input("Ingrese el usuario: ")
    clave_ingresada=input("Ingrese la clave: ")
    if not validar_clave(usuario_ingresado, clave_ingresada):
        intentos=intentos-1
    else:
        break
if intentos==0:
    print("tarjeta bloqueada")
    