billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_inicial_cajero = sum(valor * cantidad for valor, cantidad in billetes_disponibles.items())
saldo_inicial_usuario = 100000
intentos_fallidos = 0

def ingresar_usuario():
    return input("Ingrese su usuario: ")

def ingresar_clave():
    return input("Ingrese su clave: ")

def validar_usuario(usuario):
    return usuario == "10334151"

def validar_clave(clave):
    return clave == "1803"

def verificar_saldo_suficiente(saldo, monto):
    return saldo >= monto

def realizar_retiro(saldo, monto):
    return saldo - monto

def actualizar_cajero(monto):
    global saldo_inicial_cajero
    billetes_retirados = {}

    for valor, cantidad in sorted(billetes_disponibles.items(), reverse=True):
        if monto >= valor:
            cantidad_retirar = min(cantidad, monto // valor)
            monto -= valor * cantidad_retirar
            billetes_disponibles[valor] -= cantidad_retirar
            billetes_retirados[valor] = cantidad_retirar

    saldo_inicial_cajero -= sum(valor * cantidad for valor, cantidad in billetes_retirados.items())
    return billetes_retirados

def bloquear_tarjeta():
    global intentos_fallidos
    intentos_fallidos = 0
    print("Tarjeta bloqueada. Contacte al banco.")

def imprimir_saldos(saldo_usuario, saldo_cajero):
    print("saldo cuenta=" + str(saldo_usuario))
    print("saldo cajero=" + str(saldo_cajero))

def imprimir_billetes(billetes_retirados):
    for valor, cantidad in billetes_retirados.items():
        print("billetes " + str(valor) + "=" + str(cantidad))

def cajero_automatico():
    global intentos_fallidos
    
    usuario = ingresar_usuario()
    clave = ingresar_clave()
    
    if validar_usuario(usuario) and validar_clave(clave):
        saldo_usuario = saldo_inicial_usuario
        intentos_fallidos = 0
        
        while True:
            monto = int(input("Ingrese el monto a retirar: "))
            
            if monto <= 0:
                print("Monto no permitido")
                continue
            
            if verificar_saldo_suficiente(saldo_usuario, monto):
                saldo_usuario = realizar_retiro(saldo_usuario, monto)
                billetes_retirados = actualizar_cajero(monto)
                imprimir_saldos(saldo_usuario, saldo_inicial_cajero)
                imprimir_billetes(billetes_retirados)
            else:
                print("Saldo insuficiente")
                continue
            
            opcion = input("¿Desea realizar otro retiro? (S/N): ")
            
            if opcion.upper() != "S":
                break
    else:
        intentos_fallidos += 1
        print("Clave inválida")
        
        if intentos_fallidos == 3:
            bloquear_tarjeta()

cajero_automatico()

