#Cajero Automático
x = int(input("ingrese el usuario :"))
c1 = 0
while c1 < 3 :
    c2 = int(input(" clave : "))
    if c2 == 1803 :
        print (" clave valida ")
        dinero = int(input(" monton a retirar :"))
        if dinero > 100000 :
            print (" monto no permitido ")

        elif dinero < 100000 :
            sacar = 100000 - dinero
            sacar2 = 1000000 - dinero
            print ("saldo cuenta = ", sacar )
            print (" saldo cajero = ", sacar2 )
            c1 = c1 + 5
    else:
        print(" clave no valida ")
        c1 = c1 + 1

if c1 == 3:
    print (" tarjeta bloqueada ")