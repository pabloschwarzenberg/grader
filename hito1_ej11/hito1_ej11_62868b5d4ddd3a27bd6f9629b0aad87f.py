#Cajero Automático
real_usuario=10334151
saldo_cajero=1000000
saldo_cuenta=100000
real_clave=1803
contador=0
a=1
v=0
d=0
c=0

usuario=int(input("bienvenido , ingresa tu usuario:"))
while a==1:
    if usuario==real_usuario:
        clave = int(input("ingresa tu clave:"))
        while clave != real_clave and contador < 2:
            print("clave inválida")
            clave=int(input("ingresa tu clave:"))
            contador += 1
            if contador==2:
                print("tarjeta bloqueada")
                a=2
                break
        while clave==real_clave:
            monto=int(input("ingrese monto a retirar:"))
            if monto>saldo_cuenta or monto%5!=0 or monto<=5000:
                print("monto no permitido")
                a=2
                break
            else:
                print("saldo cuenta=",saldo_cuenta-monto)
                print("saldo cajero=",saldo_cajero-monto)
                saldo_cuenta-=monto
                while monto>1:
                    if monto>20000:
                        monto-=20000
                        v+=1
                    elif 20000>monto>=10000:
                        monto-=10000
                        d+=1
                    else:
                        monto-=5000
                        c+=1
                print("billetes 20000=",v)
                print("billetes 10000=",d)
                print("billetes 5000=",c)

                op=(input("desea otra operación? Para seguir presione n y si desea salir presiona otra cosa"))
                if op!="n":
                    a=2
                    break
                
    else:
        usuario=int(input("ingresa un usuario valido:"))    