#Cajero Automático
cuenta = 100000
saldo_inicial = 1000000
intentos_fallidos = 0

while True:
        usuario = (input("Ingrese su número de usuario: "))
        clave = (input("Ingrese su clave: "))
            
        if usuario == "10334151" and clave == "1803":
            break
        else:
            intentos_fallidos += 1
            print("Clave inválida")
                
            if intentos_fallidos == 3:
                print("Tarjeta bloqueada")
        
while True:
        monto = int(input('Ingresa el monto a retirar: '))

        if monto <= 0:
                print("Monto no valido")
        elif monto > cuenta or monto > saldo_inicial:
                print("No hay saldo suficiente")
        else:
            cuenta -= monto
            saldo_inicial -= monto
            print(['saldo cuenta=' + str(cuenta), 'saldo cajero=' + str(saldo_inicial)])
            opcion = str('Ingrese una letra distinta a n para salir: ')
            
        if opcion != "n":
            break
