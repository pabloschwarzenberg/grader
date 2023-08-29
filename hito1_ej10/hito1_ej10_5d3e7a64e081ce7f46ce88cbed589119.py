#Cajero Automático
cajero = 1000000
usuario = 100000


numeropersona = int(input("ingrese usuario"))

contraseña = int(input("ingrese su contraseña:"))
intentos = 2

while numeropersona != 10334151:
    numeropersona = int(input("ingrese usuario"))
    break

    
if contraseña == 1803 :
    c = int(input("monto a retirar"))

    if c < 100000:
        print("saldo cuenta =",usuario - c)
        print("saldo cajero =",cajero - c)
    
    elif c > 100000:
        print("monto no valido")



while contraseña != 1803:
    print("clave invalida")
    contraseña = int(input("ingrese su contraseña:"))
    intentos = intentos - 1
   
    if contraseña == 1803:
       cantidad = int(input("cuanto dinero quieres retirar"))
       if cantidad < 100000:
            print(usuario - cantidad)
            print(cajero - cantidad)
            break
       elif cantidad > 100000:
            print("monto no valido")
            break
    
       elif intentos == 0:
            print("tarjeta bloqueada")
            break
       break     