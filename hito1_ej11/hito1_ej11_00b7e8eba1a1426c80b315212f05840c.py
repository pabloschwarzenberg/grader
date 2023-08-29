print("Bienvenido usuario 10334151")
contador = 1
tipc=0.0
#clave = 1803
saldocajero = 1000000
saldoi = 100000
while contador >= 1:
     contador = contador + 1
     clave = int(input("ingrese la clave : "))
     if clave == 1803:
        print("Su saldo actual es de $ 100.000 ")
        monto = int(input("Monto a retirar : "))
        saldocajeroa = saldocajero - monto
        saldof = 100000 - monto
        print("1. billetes de 20.000")
        print("2. Billetes de 10.000")
        print("3. Billetes de 5.000")
        tipc = int(input('Ingrese cambio: '))
        if monto > 0 :
          if tipc == 1:
            bill20 = round(monto/20000)
            print("Saldo cuenta = ", saldof)
            print("Saldo cajero = ", saldocajeroa)
            print("Billetes de 20000 =", bill20)
          elif tipc == 2:
            bill10 = round(monto/10000)
            print("Saldo cuenta = ", saldof)
            print("Saldo cajero = ", saldocajeroa)
            print("Billetes de 10000 =", bill10)
          elif tipc ==3 :
            bill5= round(monto/5000)
            print("Saldo cuenta = ", saldof)
            print("Saldo cajero = ", saldocajeroa)
            print("Billetes de 5000 =", bill5)
          else :
            print("Opcion no valida")
          break
        elif  monto > 100000 :
          print("Monto no valido ")
     if contador > 3:
        print("tarjeta bloqueada ")
        break