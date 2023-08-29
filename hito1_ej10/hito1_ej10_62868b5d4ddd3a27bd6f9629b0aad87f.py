real_usuario=10334151
saldo_cajero=1000000
saldo_cuenta=100000
real_clave=1803
contador=0
a=1
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
            if monto>saldo_cuenta and monto!=0:
                print("monto no permitido")
                a=2
                break
            else:
                print("saldo cuenta=",saldo_cuenta-monto)
                print("saldo cajero=",saldo_cajero-monto)
                op=(input("desea otra operación? Para cerrar presione n y si desea continuar presiona otra cosa"))
                if op=="n":
                    a=2
                    break
                else:
                  a=2
                  break
    else:
        usuario=int(input("ingresa un usuario valido:"))



