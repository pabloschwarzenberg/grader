#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
intentos_fallidos = 0
billetes_disponibles = {
    20000: 20,
    10000: 40,
    5000: 40
}

def imprimir_distribucion_billetes(distribucion):
    for billete, cantidad in distribucion.items():
        print("billetes {}={}".format(billete, cantidad))

usuario = "10334151"
clave = "1803"

print("Bienvenido al cajero automático")

while True:
    ingreso_usuario = input("Ingrese su usuario: ")
    ingreso_clave = input("Ingrese su clave: ")

    if ingreso_usuario == usuario and ingreso_clave == clave:
        print("Inicio de sesión exitoso")
        saldo_actual = saldo_cuenta
        intentos_fallidos = 0
        
        while True:
            monto_retiro = float(input("Ingrese el monto a retirar: "))
            
            if monto_retiro <= saldo_actual:
                if monto_retiro > 0:
                    saldo_actual -= monto_retiro
                    saldo_cajero -= monto_retiro
                    print("Retiro exitoso")
                    print("Saldo cuenta =", saldo_actual)
                    print("Saldo cajero =", saldo_cajero)
                    
                    # Distribución de billetes
                    distribucion_billetes = {}
                    for billete, cantidad in billetes_disponibles.items():
                        if monto_retiro >= billete:
                            cant_billetes = min(cantidad, monto_retiro // billete)
                            distribucion_billetes[billete] = cant_billetes
                            monto_retiro -= cant_billetes * billete
                            billetes_disponibles[billete] -= cant_billetes
                    imprimir_distribucion_billetes(distribucion_billetes)
                    
                else:
                    print("Monto no permitido")
            else:
                print("Saldo insuficiente")
            
            continuar = input("¿Desea realizar otro retiro? (N para salir): ")
            if continuar != "N":
                break
        
    else:
        intentos_fallidos += 1
        print("Clave inválida")
        
        if intentos_fallidos == 3:
            print("Tarjeta bloqueada")
            break
