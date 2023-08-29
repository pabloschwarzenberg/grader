#Cajero Automático
u=10334151
c=1803
def validar_clave(u,clave):
    if clave!=str(c):
        print("clave invalida")
        return False
    else:
        m=input()
        if int(m)>100000:
            print("monto no permitido")
            return False
        else:
            r=1000000-int(m)
            rc=100000-int(m)
            print("saldo cuenta="+str(rc))
            print("saldo cajero="+str(r))
            return True

intentos=3
while intentos>0:
    usuario=input()
    clave2=input()
    if not validar_clave(usuario,clave2):
        intentos=intentos-1
    else:
        break
if intentos==0:
    print("tarjeta bloqueada")
    