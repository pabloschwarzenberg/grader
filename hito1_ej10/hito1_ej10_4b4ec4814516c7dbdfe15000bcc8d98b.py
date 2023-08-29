import sys
    
usuario=str(input("Ingrese su numero de usuario: "))
clave=str(input("Ingrese su clave: "))

intentos=0

while clave!="1803":
    print("clave invalida")
    intentos=intentos + 1
    if intentos==3:
        print("Targeta bloqueada")
        sys.exit(0)
    else:
        clave=str(input("Ingrese su clave nuevamente: "))
        
x=int(input("Ingrese monto a retirar: "))
    
if x>0 and x<100000:
    print("saldo cuenta=",100000-x)
    print("saldo cajero=",1000000-x)
    cierre=str(input("Para terminar ingrese algo distinto a la letra N: "))
else:
    print("monto no permitido")
    x=int(input("Ingrese monto a retirar nuevamente: "))
       
