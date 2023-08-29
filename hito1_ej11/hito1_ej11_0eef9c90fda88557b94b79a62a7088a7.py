#Cajero Automático
billetes_20 = 20
billetes_10 = 40
billetes_5 = 40
valor20 = billetes_20 * 20000
valor10 = billetes_10 * 10000
valor5 = billetes_5 * 5000




saldo_inicial_cajero = valor10 + valor20 + valor5
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
retira = monto_a_retirar 
billetes20_a_dar = 0
billetes10_a_dar = 0
billetes5_a_dar = 0

while retira !=0:
   
    if retira >= 20000:
        billetes20_a_dar += 1
        retira -= 20000
        billetes_20 -= 1
    elif 10000 <= retira <20000:
        billetes10_a_dar += 1
        retira -= 10000
        billetes_10 -=1
    elif 5000 <= retira < 10000:
        billetes5_a_dar += 1
        retira -= 5000 
        billetes_5 -= 1
saldo_persona = 100000 - monto_a_retirar
saldo_inicial_cajero = 1000000 - monto_a_retirar
print("[saldo cuenta=", saldo_persona, "saldo cajero=", str(saldo_inicial_cajero)+"]")

print("Billetes 20000=", billetes20_a_dar)
print("Billetes 10000=", billetes10_a_dar)
print("Billetes 5000=", billetes5_a_dar)
