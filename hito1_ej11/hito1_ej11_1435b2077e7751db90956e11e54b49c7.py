import sys

def cajero():
    saldo_cuenta = 100000
    saldo_cajero = {
        20000: 20,
        10000: 40,
        5000: 40
    }
    intentos = 0
    
    usuario_correcto = "10334151"
    clave_correcta = "1803"
    
    while intentos < 3:
        entrada = sys.stdin.readline().strip()
        valores = entrada.split()
        
        if len(valores) < 3:
            print("Debe ingresar los valores requeridos.")
            continue
        
        usuario = valores[0]
        clave = valores[1]
        monto = valores[2]
        
        if usuario == usuario_correcto and clave == clave_correcta:
            break
        else:
            print("Clave inválida")
            intentos += 1
            
    if intentos == 3:
        print("Tarjeta bloqueada")
        return
    
    monto = float(monto)
    
    if monto > saldo_cuenta:
        print("Monto no permitido")
    else:
        billetes_entregados = {}
        
        for denominacion, cantidad in saldo_cajero.items():
            if monto >= denominacion and cantidad > 0:
                cantidad_billetes = min(monto // denominacion, cantidad)
                billetes_entregados[denominacion] = cantidad_billetes
                monto -= denominacion * cantidad_billetes
                saldo_cajero[denominacion] -= cantidad_billetes
        
        if monto > 0:
            print("No es posible entregar el monto solicitado con los billetes disponibles.")
        else:
            saldo_cuenta -= monto
            print("saldo cuenta={}".format(saldo_cuenta))
            print("saldo cajero={}".format(saldo_cajero))
            print("Billetes entregados:")
            for denominacion, cantidad in billetes_entregados.items():
                print("billetes {}={}".format(denominacion, cantidad))

cajero()
