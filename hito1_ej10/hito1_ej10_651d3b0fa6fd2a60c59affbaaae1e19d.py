usuario_r= "10334151"
clave_r= "1803"
Saldo_c=1000000
Saldo_u=100000
def Validar(usuario,clave):
    if usuario!=usuario_r or clave!=clave_r:
        print("clave invalida")
        return False
    else:
        return True
def Validar_monto(retiro):
    if retiro>Saldo_c or retiro>Saldo_u:
        return False
    else:
        return True
usuario=""
if usuario!="N":
    intentos=3
    while intentos>0:
        usuario=input()
        clave=input()
        if Validar(usuario,clave)==False:
            intentos-=1
            
        else:
            retirar=int(input())
            if Validar_monto(retirar)==False:
                print("monto no permitido")
            else:
                Saldo_c-=retirar
                Saldo_u-=retirar
                print("saldo cuenta=",Saldo_u, "saldo cajero=",Saldo_c)                               
            break
    if intentos==0:
       print("tarjeta bloqueda")
        
else:
    False
