#Cajero Automático
saldo_inicial = 1000000
saldo_cajero = saldo_inicial
usuario_valido = 10334151
clave_valida = 1803
intentos_fallidos = 0

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))
    
    if usuario == usuario_valido and clave == clave_valida:
        saldo_usuario = 100000
        print("Inicio de sesión exitoso.")
        break
    
    else:
        print("Usuario o clave incorrectos.")
        intentos_fallidos += 1
        
    if intentos_fallidos == 3:
        print("Tarjerta bloqueada.")
        exit()
        
while True:
    monto_retiro = int(input("Ingrese el monto a retirar: "))
    
    if monto_retiro > saldo_usuario:
        print("Monto no permitido. Fondos insuficientes.")
    
    elif monto_retiro > saldo_cajero:
        print("Monto no permitido. Cajero sin fondos suficientes.")
    else:
        saldo_usuario -= monto_retiro
        saldo_cajero -= monto_retiro
        print("Retiro exitoso.")
        print("Saldo cuenta= {}".format(saldo_usuario))
        print("Saldo cajero= {}".format(saldo_cajero))
        
    opcion = input("¿Desea realizar otro retiro? (S/N): ")
    if opcion.upper() != "S":
        break
        
       
       