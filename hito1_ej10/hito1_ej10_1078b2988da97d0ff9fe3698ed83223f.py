#Cajero Automático
saldocajero = 1000000
saldocuenta = 100000
clavereal = 1803
usuario = 10334151

t = True
contador_de_errores = 0

while t:
    user = input("Ingrese usuario: ")
    if user == "N":
        t = False
    else:
        clave = int(input("Ingrese clave: "))
        monto = int(input("Ingrese monto a retirar: "))
        nUser = int(user)
        if nUser == usuario:
            if clave == clavereal:
                if monto <= saldocuenta:
                    print("Saldo cuenta =",saldocuenta - monto)
                    print("Saldo cajero =",saldocajero - monto)
                else:
                    print("monto no permitido")   
        
                
            else:
                print("Clave inválida")
                contador_de_errores += 1
                if contador_de_errores == 3:
                    print("Tarjeta bloqueada")
                    t = False
        
        else:
            print("Usuario inválido")