cajero = 1000000
intentos = 0
usuario = ['10334151', '1803', 100000]
while intentos < 3:
    if __name__ == "__main__":
        user = input("Ingrese el usuario: ")
        pasw = input("Ingrese el password: ")
        if user == usuario[0] and pasw == usuario[1]:
            monto = int(input("Ingresa el monto a retirar: "))
            if monto < usuario[2]:
                usuario[2] -= monto
                cajero -= monto
                print("saldo cuenta=" + str(usuario[2]) + ", saldo cajero=" + str(cajero))
            else:
                print("monto no permitido")
        else:
            print("clave inválida")
            intentos += 1
else:
    print("tarjeta bloqueada")