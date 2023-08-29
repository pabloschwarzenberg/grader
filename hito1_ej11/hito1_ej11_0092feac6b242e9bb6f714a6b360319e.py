saldo_cuenta = 1000000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

def mostrar_saldos():
    print("Saldo de cuenta:", saldo_cuenta)
    print("Saldo de billetes en el cajero:")
    for denominacion, cantidad in saldo_cajero.items():
        print("Billetes de", denominacion, "=", denominacion * cantidad)

def realizar_retiro(monto):
    global saldo_cuenta, saldo_cajero
    billetes_entregados = {}
    
    for denominacion in sorted(saldo_cajero.keys(), reverse=True):
        cantidad_billetes = min(monto // denominacion, saldo_cajero[denominacion])
        monto -= cantidad_billetes * denominacion
        saldo_cajero[denominacion] -= cantidad_billetes
        
        if cantidad_billetes > 0:
            billetes_entregados[denominacion] = cantidad_billetes
    
    if monto == 0:
        print("Retiro exitoso")
        print("Billetes entregados:")
        for denominacion, cantidad in billetes_entregados.items():
            print("Billetes de", denominacion, "=", cantidad)
        saldo_cuenta -= sum(billetes_entregados.values()) * sum(billetes_entregados.keys())
    else:
        print("No se pudo realizar el retiro. Monto no disponible")

# Ejemplo de uso
print("Bienvenido al cajero automático")
mostrar_saldos()

monto_retiro = int(input("Ingrese el monto a retirar: "))
realizar_retiro(monto_retiro)

print("Saldo actualizado:")
mostrar_saldos()

