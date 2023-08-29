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
            veinte=0
            d=int(m)
            while d//20000!=0 and int(m)!=20000:
                d=d//20000
                veinte=veinte+d
            diez=0 
            d=int(m)-veinte*20000
            while d//10000!=0 and int(m)!=10000:
                d=d//10000
                diez=diez+d
            cinco=0
            d=int(m)-veinte*20000-diez*10000
            while d//5000!=0 and int(m)!=5000:
                d=d//5000
                cinco=cinco+d
            r=1000000-int(m)
            rc=100000-int(m)
            print("billetes 20000="+str(veinte))
            print("billetes 10000="+str(diez))
            print("billetes 5000="+str(cinco))
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
    