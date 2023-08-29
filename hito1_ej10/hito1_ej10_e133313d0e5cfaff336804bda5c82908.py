#Cajero Automático
usuario="10334151"
clave="1803"

def validar_clave(usuario,clave_ingresada):
    if clave_ingresada==clave:
        print("Bienvenido")
        return True
    else:
        print("Clave Incorrecta")
        return False
    
intentos=3
while intentos>0:
    usuario_ingresado=input("Ingrese su usuario: ")
    clave_ingresada=input("Ingrese su clave: ")
    if not validar_clave(usuario_ingresado,clave_ingresada):
        intentos=intentos-1
    else:
        break
if intentos==0:
    print("Clave bloqueada")
    
monto=int(input("ingrese el monto a retirar: "))
    if monto <= 55000:
    print("retirar monto")
    elif monto > 55000:
    return False
  