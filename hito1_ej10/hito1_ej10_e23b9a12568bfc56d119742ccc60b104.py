#Cajero Automático
usuario=int(input("Ingrese usuario: "))
clave=int(input("Ingrese clave: "))
intentos=3
saldo_cajero=1000000
saldo_usuario=100000
usuario1= 10334151
password= 1803
while clave!=password:
    intentos-1
    if clave==password:
        break
        print("Clave incorrecta")
    if intentos==0:
        break
        
    print("Clave inválida")
    clave=int(input("Intente de nuevo, Ingrese su clave: "))
if intentos==0:
    print("Tarjeta bloqueada")
if usuario==usuario1:
    if clave==password:
        monto=int(input("¿Cuánto desea retirar?: "))
        if monto>saldo_usuario and monto>saldo_cajero:
            print("Monto no permitido")
        else:
            saldo_usuario=saldo_usuario-monto
            saldo_cajero=saldo_cajero-monto
            print("Saldo cuenta= ",saldo_usuario)
            print("Saldo cajero= ",saldo_cajero)

    
