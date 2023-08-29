print("Inserte usuario")
u=int(input("Usuario="))
i=0
b_20=20
b_10=40
b_5=40
if u==10334151:
    while i<3:
        print("Inserte clave de 4 digitos")
        c=int(input("clave="))
        if c==1803:
            print("inserte monto a retirar")
            m = int(input("monto:"))
            if m > 100000 or m%5000 !=0:
                print("monto no permitido")
            elif m <= 100000 and m>0:
                 scu=(100000-m)
                 sca=(1000000-m)
                    a = 0
                    while a < n_20:
                        if monto < 20000:
                            break
                        else:
                            monto = monto - 20000
                            a = a + 1
                    b = 0
                    while b < n_10:
 
                        if monto < 10000:
                            break
                        else:
                            monto = monto - 10000
                            b = b + 1
                    c = 0
                    while c < n_5:
                        if monto < 5000:
                            break
                        else:
                            monto = monto - 5000
                            c = c + 1

                    if a != 0:
                        print('billetes 20000='+str(a))
                    if b != 0:
                        print('billets 10000='+str(b))
                    if c != 0:
                        print('billetes 5000='+str(c))

                    n_20 = n_20-a
                    n_10 = n_10-b
                    n_5 = n_5-c
   
                print("saldocuenta=",scu,",","saldocajero=",sca)
        else:
            print("clave invalida")
            i=i+1
            if i==3:
                print("tarjeta bloqueda")
else:
    print("usuario incorrecto")

