#Cajero Automático
usuario="10334151"
clave="1803"
monto=""
saldo_cuenta=1000000

def validar_clave(usuario,clave_ingresada):
    if clave_ingresada==clave:
        print("Bienvenido!")
        print("Por favor, ingrese monto.")
        str(saldo_cajero=saldo_cuenta-monto)
        return True
    else:
        print("Clave incorrecta.")
        return False

intentos=3
while intentos>0:
    usuario_ingresado=input("Ingrese su usuario: ")
    clave_ingresada=input("Ingrese su contraseña: ")
    if not validar_clave(usuario_ingresado,clave_ingresada):
        intentos=intentos-1
    else:
        break
if intentos==0:
    print("Clave bloqueada.")
     