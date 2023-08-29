#Cajero Automático
print("Bienvenido usuario 10334151")
contador = 1
#clave = 1803
saldocajero = 1000000
saldoi = 100000
while contador >= 1:
     contador = contador + 1
     clave = int(input("ingrese la clave : "))
     if clave == 1803:
        print("Su saldo actual es de $ 100.000 ")
        monto = int(input("Monto a retirar : "))
        if monto > 0 :
          saldocajeroa = saldocajero - monto
          saldof = 100000 - monto
          print("Saldo cuenta = ", saldof)
          print("Saldo cajero = ", saldocajeroa)
          break
        elif  monto > 100000 :
          print("Monto no valido ")
     if contador > 3:
        print("tarjeta bloqueada ")
        break      