#Cajero Automático
usuario="10334151"
clave="1803"
saldo_cajero=1000000
saldo_usuario_inicial=100000



def validar_clave(clave_ingresada):
    global saldo_cajero
    if clave_ingresada==clave:
        print("Bienvenido")
    else:
        print("Clave Incorrecta")
        return False
    
    monto_retirar=int(input("Ingrese monto: "))
    if monto_retirar>saldo_usuario_inicial:
        print("monto no permitido")
    else:
        saldo_usuario=saldo_usuario_inicial - monto_retirar
        saldo_cajero=saldo_cajero - monto_retirar
        print("saldo cuenta="+str(saldo_usuario))
        print("saldo cajero="+str(saldo_cajero))
        return True
        
    
usuario_ingresado=input("Ingrese su usuario: ")
while not usuario_ingresado==usuario:
    usuario_ingresado=input("Ingrese su usuario: ")

intentos=3
while intentos>0:
    clave_ingresada=input("Ingrese su clave: ")
    if not validar_clave(clave_ingresada):
        intentos=intentos-1
    else:
        break
if intentos==0:
    print("Clave bloqueada") 