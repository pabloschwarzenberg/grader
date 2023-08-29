#Cajero Automático
def validar_usuario(usuario, clave):
    return usuario == "10334151" and clave == "1803"

def retirar_dinero(saldo_cuenta, monto):
    if monto > saldo_cuenta or monto % 10000 != 0:
        print("Monto no permitido")
        return saldo_cuenta
    
    saldo_cuenta -= monto
    return saldo_cuenta

saldo_cajero = 1000000
saldo_cuenta = 100000
intentos = 0

while True:
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")

    if validar_usuario(usuario, clave):
        while True:
            monto = int(input("Ingrese el monto a retirar (múltiplo de 10.000): "))
            if monto > 0:
                saldo_cuenta = retirar_dinero(saldo_cuenta, monto)
                print(f"Saldo cuenta: {saldo_cuenta}")
                saldo_cajero -= monto
                print(f"Saldo cajero: {saldo_cajero}")
                break
            else:
                print("Monto inválido")
    else:
        intentos += 1
        print("Clave inválida")
        
        if intentos == 3:
            print("Tarjeta bloqueada")
            break
      