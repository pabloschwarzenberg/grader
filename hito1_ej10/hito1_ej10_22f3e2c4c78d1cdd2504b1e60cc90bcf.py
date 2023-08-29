#Cajero Automático
usuario_valido = "10334151"
clave_valida = "1803"
saldo_usuario = 100000
saldo_cajero = 1000000

intentos_fallidos = 0

while True:
   
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        intentos_fallidos = 0
       
        monto = float(input("Ingrese el monto a retirar: "))

        if monto <= saldo_usuario:
         
            saldo_usuario -= monto
            saldo_cajero -= monto

          
            print("saldo cuenta =", saldo_usuario)
            print("saldo cajero =", saldo_cajero)
        else:
            print("Monto no permitido")
    else:
      
        intentos_fallidos += 1

        
        if intentos_fallidos >= 3:
            print("Tarjeta bloqueada")
            break
        else:
            print("Clave inválida")

    opcion = input("¿Desea realizar otra transacción? (S/N): ")
    if opcion.upper() != "S":
        break     