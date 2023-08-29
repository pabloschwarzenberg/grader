u = input("Usuario: ")
c = int(input("Clave: "))
scuenta = 1000000
scajero = 100000
if c != 1803 :
    print ("clave invalida")
else :
    m = int(input("Ingrese monto a retirar: ")
            if m > scuenta and m > scajero :
                print ("monto no permitido")
            else :
                nuevscuenta = scuenta - m
                nuevscajero = scajero - m
                print ("saldo cuenta=", nuevscuenta)
                print ("saldo cajero=", nuevscajero)
c = int(input("Clave: "))
if c != 1803 :
    print ("clave invalida")
else :
    m = int(input("Ingrese monto a retirar: ")
            if m > scuenta or m > scajero :
                print ("monto no permitido")
            else :
                nuevscuenta = scuenta - m
                nuevscajero = scajero - m
                print ("saldo cuenta=", nuevscuenta)
                print ("saldo cajero=", nuevscajero)
c = int(input("Clave: "))
if c != 1803 :
    print ("tarjeta bloqueada")