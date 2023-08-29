saldo_cajero = 1000000
saldo_inicial = 100000
intentos = 3
A = "N"

while True:
    Usuario = int(input("Ingrese su Usuario: "))
    Clave = int(input("Ingrese la Clave: "))
    
    if Usuario == 10334151 and Clave == 1803:
        print("Bienvenido")
        saldo_actual = saldo_inicial
        
        while intentos > 0:
            monto_retiro = int(input("Ingrese el monto a retirar: "))
            
            if monto_retiro <= saldo_actual:
                saldo_actual -= monto_retiro
                saldo_cajero -= monto_retiro
                print("Saldo cuenta =", saldo_actual)
                print("Saldo cajero =", saldo_cajero)
                break
            else:
                print("Monto no permitido")
            
            intentos -= 1

        if intentos == 0:
            print("Tarjeta bloqueada")
            break
    else:
        print("Clave inválida")
        
    A = input("Presione 'N' para continuar o cualquier otra tecla para salir: ")
    
    if A != "N":
        print("Usted ha salido del programa")
        break
