usuario = int(input("Ingrese su número de usuario: "))
clavewena = 1803
montoinicial = 1000000
saldocuenta = 100000


tries = 0
p = True

while p:
    tries += 1
    if tries <= 3:
        clave = int(input("Ingrese su clave: "))
        if clavewena == clave:
            print("Tienes", saldocuenta,"en tu cuenta")
            
            
            
            montoasacar = int(input("Indique monto a retirar: "))
            if montoasacar <= saldocuenta:
                print("Saldo cuenta = ", saldocuenta - montoasacar)
                print("Saldo cajero = ", montoinicial - montoasacar)
                p = False

            
    else: 
        print("Clave inválida, tarjeta bloqueada")
        p = False
