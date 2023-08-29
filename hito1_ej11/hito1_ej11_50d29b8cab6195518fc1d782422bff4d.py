def cajero(saldo_inicial):
    # Define los billetes disponibles
    billetes = [20000, 10000, 5000]
    cantidades = [20, 40, 40]
    saldo = saldo_inicial
    
    # Imprime el saldo inicial
    print("Saldo inicial:", saldo)
    
    # Pide al usuario que ingrese la cantidad a retirar
    retiro = input("Ingrese la cantidad a retirar: ")
    
    # Verifica si el retiro es mayor que el saldo disponible
    if int(retiro) > saldo:
        print("Fondos insuficientes")
        return
    
    # Distribuye el monto a retirar entre los diferentes billetes disponibles
    billetes_entregados = []
    for i in range(len(billetes)):
        cantidad_billetes = min(int(retiro) // billetes[i], cantidades[i])
        retiro = int(retiro) - cantidad_billetes * billetes[i]
        cantidades[i] -= cantidad_billetes
        billetes_entregados.append(cantidad_billetes)
    
    # Imprime la cantidad de billetes entregados
    for i in range(len(billetes)):
        if billetes_entregados[i] > 0:
            print("billetes", billetes[i], "=", billetes_entregados[i])
    
    # Imprime el saldo restante
    print("Saldo restante:", saldo - saldo_inicial + int(retiro))
    
    # Imprime el saldo de la cuenta y del cajero
    print(["saldo cuenta=" + str(saldo - int(retiro)), "saldo cajero=" + str(sum(billete*cantidad for billete, cantidad in zip(billetes, cantidades)))])
    

if __name__ == "__main__":
    cajero(1000000)











