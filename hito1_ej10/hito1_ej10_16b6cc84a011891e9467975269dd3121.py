cajero = 1000000
saldo = 100000
i = 0  

while i <= 3:
    usuario = eval(input("Ingresar usuario: ")) 
    clave = eval(input("Ingresar clave: "))    
    i = i + 1
    if usuario == 10334151 and clave == 1803:
        monto = eval(input("Ingresar monto de retiro: "))

        if monto <= saldo:
            cajero = cajero - monto
            saldo = saldo - monto
            print("saldo cuenta=",saldo)
            print("saldo cajero=",cajero)
            break
        else:
            print("monto no permitido")
    else:
        print("clave invalida")
    if i == 3:
        print("tarjeta bloqueada")
    