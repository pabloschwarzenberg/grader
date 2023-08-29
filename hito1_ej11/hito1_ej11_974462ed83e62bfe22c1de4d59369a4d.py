usuario = int(input("Ingrese su número de usuario: "))
clavewena = 1803
montoinicial = 1000000
saldocuenta = 100000


#division qlia de billetes


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
                #division qlia de billetes
                billete20 = int(montoasacar/20000)
                montoasacar = montoasacar%20000
                billete10 = int(montoasacar/10000)
                montoasacar = montoasacar%10000
                billete5 = int(montoasacar/5000)
                montoasacar = montoasacar%5000

                
                
                print("Billetes 20000 = ", billete20    )
                print("Billetes 10000 = ", billete10   )
                print("Billetes 5000 = ", billete5    )
                
                
                
                
                p = False

            
    else: 
        print("Clave inválida, tarjeta bloqueada")
        p = False
