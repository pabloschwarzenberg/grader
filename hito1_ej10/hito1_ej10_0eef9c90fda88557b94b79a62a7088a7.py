#Cajero Automático
saldo_inicial_cajero = 1000000
saldo_persona = 100000
intento = 0
usuario = "10334151"
clave = "1803"
dinero_usuario = 100000
usuario_ing = False
clave_ing = False
ingreso = False

pedir_usuario = input("Ingrese su nro de cuenta: ")
if pedir_usuario != usuario:
    while True:
        pedir_usuario = input("Usuario no existe ingrese otro: ")
        if pedir_usuario == usuario:
            usuario_ing = True
            break
        else: 
            pass
else :
    usuario_ing = True
while intento < 3:
    pedir_clave = input("ingresa tu clave: ")
    intento += 1
    if pedir_clave == clave:
        clave_ing = True
        break
    elif intento == 3:
        print("trajeta bloqueada")
        exit()

if (clave_ing == True) and usuario_ing == True:
    while True:
        monto_a_retirar = int(input("Cuanto dinero deseas retirar: "))
        if monto_a_retirar > saldo_inicial_cajero or monto_a_retirar > saldo_persona:
            print("Monto no permitido, ingrese otro")
        elif monto_a_retirar < saldo_persona or monto_a_retirar < saldo_inicial_cajero:
            break
saldo_inicial_cajero -= monto_a_retirar
saldo_persona -= monto_a_retirar
print("saldo cuenta=", saldo_persona, "saldo cajero=", saldo_inicial_cajero,"]")