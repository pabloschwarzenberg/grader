usuario="10334151"
clave="1803"

def validar_clave(usuario,clave_ingresada):
    if clave_ingresada==clave:
        
        return True
    else:
        print("clave invalida")
        return False
intentos=3
while intentos>0:
    usuario_ingresado=input("ingrese su usuario:")
    clave_ingresada=input("ingrese su clave:")

    if not validar_clave(usuario_ingresado,clave_ingresada):
        intentos=intentos-1
    else:
        break
    
if intentos==0:
    print("tarjeta bloqueada")
    
if intentos>0:
    x=int(input("ingrese el monto que desea retirar:"))
    if x>100000:
        print("monto no permitido")
    else:
        
        a=x//20000
        b=x%20000
        c=b//10000
        d=b%10000
        e=d//5000
        
        print("saldo cuenta= ",100000-x)
        print("saldo cajero= ",1000000-x)
        print("billetes 20000= ",a)
        print("billetes 10000= ",c)
        print("billetes 5000= ",e)
      