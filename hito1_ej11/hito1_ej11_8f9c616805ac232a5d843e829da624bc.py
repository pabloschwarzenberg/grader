#Cajero Automático
def verificar_clave(usuario, clave):
    if usuario == "10334151" and clave == "1803":
        return True
    else:
        return False

saldo_cuenta = 100000
saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

usuario = "10334151"
clave = "1803"
monto_retiro = 20000

if verificar_clave(usuario, clave):
    if monto_retiro <= saldo_cuenta and monto_retiro > 0:
        billetes_entregados = {}

        for denominacion in sorted(saldo_cajero.keys(), reverse=True):
            cantidad_disponible = saldo_cajero[denominacion]
            cantidad_billetes = min(monto_retiro // denominacion, cantidad_disponible)
            monto_retiro -= cantidad_billetes * denominacion
            saldo_cajero[denominacion] -= cantidad_billetes
            if cantidad_billetes > 0:
                billetes_entregados[denominacion] = cantidad_billetes

        saldo_cuenta -= monto_retiro
        print("Retiro exitoso.")

        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)

        if sum(billetes_entregados.values()) > 0:
            print("Billetes entregados:")
            for denominacion, cantidad_billetes in billetes_entregados.items():
                print("Billetes", denominacion, "=", cantidad_billetes)
        else:
            print("No se entregaron billetes.")
    else:
        print("Monto no permitido.")
        print("Saldo cuenta =", saldo_cuenta)
        print("Saldo cajero =", saldo_cajero)
else:
    print("Clave inválida.")
