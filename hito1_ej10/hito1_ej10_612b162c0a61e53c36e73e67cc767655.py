#Cajero Automático
print("Bienvenido")

u=int(input("Ingrese número de usuario:"))
if u==10334151:
    veces=3
    while veces>0:
        clave=(input("Ingrese clave:"))
        if clave !="1803":
            print("clave inválida")
            veces=veces-1
            if veces==0:
                print("TARJETA BLOQUEADA")
                e=input("Salir:")
                if e !="N":
                    break
        if clave=="1803":
             print("Tiene un saldo de 100000")
             m=int(input("Ingrese monto a retirar:"))
                if m==45000:
                    print("Saldo cuenta:",100000-45000)
                    print("Saldo cajero:",1000000-45000)
                
                if m==20000:
                    print("Saldo cuenta:",100000-20000)
                    print("Saldo cajero:",1000000-20000)
                if m==10000:
                    print("Saldo cuenta:",100000-10000)
                    print("Saldo cajero:",1000000-10000)
                if m==5000:
                    print("Saldo cuenta:",100000-5000)
                    print("Saldo cajero:",1000000-5000)
                if m==2000:
                    print("Saldo cuenta:",100000-2000)
                    print("Saldo cajero:",1000000-2000)
                if m==1000:
                    print("Saldo cuenta:",100000-1000)
                    print("Saldo cajero:",1000000-1000)

                if m !=45000 and m !=20000 and m !=10000 and m != 5000 and m !=2000 and m !=1000:
                    print("Monto no permitido")
                    m=int(input("ingrese monto a retirar:"))
                
                
                      