#Cajero Automático
def retirar(monto):
    num_20000_bill = 0
    num_10000_bill = 0
    num_5000_bill = 0
    while monto > 0:
        if monto >= 20000:
            monto -= 20000
            num_20000_bill += 1
        elif monto >= 10000:
            monto -= 10000
            num_10000_bill += 1
        elif monto >= 5000:
            monto -= 5000
            num_5000_bill += 1
        else: break
    print("Billete 20000=", num_20000_bill)
    print("Billete 10000=", num_10000_bill)
    print("Billete 5000=", num_5000_bill)
Valor = 1000000
monto = int(input("Ingrese el monto: "))
retirar(monto)
print("Valor=", Valor)