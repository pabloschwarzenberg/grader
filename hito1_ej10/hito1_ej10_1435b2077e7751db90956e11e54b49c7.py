def cajero():
    saldo_cuenta = 100000
    saldo_cajero = 1000000
    intentos = 0
    
    usuario_correcto = "10334151"
    clave_correcta = "1803"
    
    while True:
        entrada = input("Ingrese su usuario, clave y monto a retirar (separados por espacios): ")
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
        saldo_cuenta -= monto
        saldo_cajero -= monto
        print("saldo cuenta={}".format(saldo_cuenta))
        print("saldo cajero={}".format(saldo_cajero))

cajero()
