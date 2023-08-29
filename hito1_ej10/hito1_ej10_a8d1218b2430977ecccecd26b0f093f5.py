#Cajero Automático
usuario = "10334151"
clave = "1803"
saldo_cuenta = 100000
saldo_cajero = 1000000

print("- Tecla N para retirar\n- Cualquier otra tecla para salir.")

intentos = 0
bloqueado = False

while True:
    opcion = input("Seleccione opción: ")
    
    if opcion.upper() != "N":
        break
    
    iu = input("Indique usuario: ")
    
    if iu != usuario:
        print("Usuario inválido")
        continue
    
    ic = input("Indique clave: ")
    
    if ic != clave:
        intentos += 1
        print("Clave inválida")
        
        if intentos >= 3:
            bloqueado = True
            print("Tarjeta bloqueada")
            break
    else:
        monto = int(input("Ingrese monto a retirar de la cuenta: "))
        
        if monto <= 0:
            print("Monto no permitido")
            continue
        
        if monto > saldo_cuenta:
            print("Saldo insuficiente")
            continue
        
        saldo_cuenta -= monto
        saldo_cajero -= monto
        
        print(f"Saldo cuenta = {saldo_cuenta}")
        print(f"Saldo cajero = {saldo_cajero}")

    print("- Tecla N para retirar\n- Cualquier otra tecla para salir.")
  